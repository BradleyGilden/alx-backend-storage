#!/usr/bin/env python3

"""
Module used for testing

Author: Bradley Dillion Gilden
Date: 24-01-2024
"""

Cache = __import__('exercise').Cache

cache = Cache()

TEST_CASES = {
    "foo": None,
    123: int,
    "bar": lambda d: d.decode("utf-8")
}

print(type(cache.get_int(cache.store("123"))))
