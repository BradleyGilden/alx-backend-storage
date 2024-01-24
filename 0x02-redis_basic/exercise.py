#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 24-01-2024
"""
import redis
from uuid import uuid4
from typing import Union, Callable, Optional


RedisTypes = Union[str, bytes, int, float]


class Cache:
    """controls cache of an application"""

    def __init__(self) -> None:
        """constructor function"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: RedisTypes) -> str:
        """stores a value assigned to a random uuid generated key"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None):
        """calls redis.get() with a function to convert the stored data"""
        if fn:
            return fn(self._redis.get(key))
        data = self._redis.get(key)
        return data

    def get_int(self, key: str) -> int:
        """get a number"""
        value = 0
        try:
            value = self.get(key, lambda d: int(d.decode('utf-8')))
        except Exception:
            value = 0
        return value

    def get_str(self, key: str) -> str:
        """get a string"""
        return self.get(key, lambda d: d.decode('utf-8'))
