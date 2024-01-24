# Redis - Basics

Redis is a popular NoSQL database where data is stored in the RAM, making it a good option to store cached data.

## Learning Objectives

* Learn how to use redis for basic operations
* Learn how to use redis as a simple cache

## Tasks

* [exercise.py](exercise.py) - 
  ### Task 1
  Create a Cache class. In the __init__ method, store an instance of the Redis client as a private variable named _redis (using redis.Redis()) and flush the instance using flushdb.
  Create a store method that takes a data argument and returns a string. The method should generate a random key (e.g. using uuid), store the input data in Redis using the random key and return the key.
  Type-annotate store correctly. Remember that data can be a str, bytes, int or float

  ### Task 2
  Redis only allows to store string, bytes and numbers (and lists thereof). Whatever you store as single elements, it will be returned as a byte string. Hence if you store "a" as a UTF-8 string, it will be returned as b"a" when retrieved from the server.
  In this exercise we will create a get method that take a key string argument and an optional Callable argument named fn. This callable will be used to convert the data back to the desired format.
  Remember to conserve the original Redis.get behavior if the key does not exist.
  Also, implement 2 new methods: get_str and get_int that will automatically parametrize Cache.get with the correct conversion function

  ### Task 3
  In this task, we will implement a system to count how many times methods of the Cache class are called.
  Above Cache define a count_calls decorator that takes a single method Callable argument and returns a Callable.
  As a key, use the qualified name of method using the __qualname__ dunder method.
  Create and return function that increments the count for that key every time the method is called and returns the value returned by the original method.
  Remember that the first argument of the wrapped function will be self which is the instance itself, which lets you access the Redis instance.
