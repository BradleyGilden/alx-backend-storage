#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 24-01-2024
"""
from redis import Redis
from uuid import uuid4
from typing import Union


class Cache:
    """controls cache of an application"""

    def __init__(self) -> None:
        """constructor function"""
        self._redis = Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores a value assigned to a random uuid generated key"""
        key = str(uuid4())
        self._redis.mset({key: data})
        return key


if __name__ == '__main__':
    cache = Cache()

    data = b"hello"
    key = cache.store(data)
    print(key)

    local_redis = Redis()
    print(local_redis.get(key))
