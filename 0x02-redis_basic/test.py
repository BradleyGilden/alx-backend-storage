#!/usr/bin/env python3

"""
Module used for testing

Author: Bradley Dillion Gilden
Date: 24-01-2024
"""

Cache = __import__('exercise').Cache

cache = Cache()

cache.store(b"first")
print(cache.get(cache.store.__qualname__))

cache.store(b"second")
cache.store(b"third")
print(cache.get(cache.store.__qualname__))
