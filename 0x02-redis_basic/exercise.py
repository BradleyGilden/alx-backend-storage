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


def replay(callable: Callable) -> None:
    """displays the history of calls of a particular functon"""
    key = callable.__qualname__
    ikey = f"{key}:inputs"
    okey = f"{key}:outputs"
    # get reference to instance that called the method
    obj = callable.__self__

    # get list of inputs and outputs while mapping data to a string
    ilist = list(
        map(lambda a: a.decode("utf-8"), obj._redis.lrange(ikey, 0, -1))
    )
    olist = list(
        map(lambda a: a.decode("utf-8"), obj._redis.lrange(okey, 0, -1))
    )
    callcount = len(ilist)
    print(f"{key} was called {callcount} times")
    for i, o in zip(ilist, olist):
        print(f"{key}(*{i}) -> {o}")


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
