#!/usr/bin/env python3

"""
Module used for testing

Author: Bradley Dillion Gilden
Date: 24-01-2024
"""

from exercise import Cache, replay

cache = Cache()

cache.store("foo")
cache.store("bar")
cache.store(42)
replay(cache.store)
