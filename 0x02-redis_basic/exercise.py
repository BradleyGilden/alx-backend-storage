#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 24-01-2024
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional
from functools import wraps


RedisTypes = Union[str, bytes, int, float]


def count_calls(method: Callable) -> Callable:
    """decorator to count number of calls to redis"""
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper to preserve original functions documentation"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    keeps track of function call inputs and their relative outputs
    in a list
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """wrapper to preserve original functions documentation"""
        self._redis.rpush(f"{key}:inputs", str(args))
        res = method(self, *args, *kwargs)
        self._redis.rpush(f"{key}:outputs", str(res))
        return res

    return wrapper


def replay(fn: Callable):
    """display the history of calls of a particular function"""
    r = redis.Redis()
    function_name = fn.__qualname__
    value = r.get(function_name)
    try:
        value = int(value.decode("utf-8"))
    except Exception:
        value = 0

    # print(f"{function_name} was called {value} times")
    print("{} was called {} times:".format(function_name, value))
    # inputs = r.lrange(f"{function_name}:inputs", 0, -1)
    inputs = r.lrange("{}:inputs".format(function_name), 0, -1)

    # outputs = r.lrange(f"{function_name}:outputs", 0, -1)
    outputs = r.lrange("{}:outputs".format(function_name), 0, -1)

    for input, output in zip(inputs, outputs):
        try:
            input = input.decode("utf-8")
        except Exception:
            input = ""

        try:
            output = output.decode("utf-8")
        except Exception:
            output = ""

        # print(f"{function_name}(*{input}) -> {output}")
        print("{}(*{}) -> {}".format(function_name, input, output))


class Cache:
    """controls cache of an application"""

    def __init__(self) -> None:
        """constructor function"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: RedisTypes) -> str:
        """stores a value assigned to a random uuid generated key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    @call_history
    @count_calls
    def get(self, key: str, fn: Optional[Callable] = None) -> RedisTypes:
        """calls redis.get() with a function to convert the stored data"""
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    @call_history
    @count_calls
    def get_int(self, key: str) -> int:
        """get a number"""
        value = 0
        try:
            value = self.get(key, lambda d: int(d.decode("utf-8")))
        except Exception:
            value = 0
        return value

    @call_history
    @count_calls
    def get_str(self, key: str) -> str:
        """get a string"""
        return self.get(key, lambda d: d.decode("utf-8"))
