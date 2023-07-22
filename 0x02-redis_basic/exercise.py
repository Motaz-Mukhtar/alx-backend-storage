#!/usr/bin/env python3
"""
    Redis Client
"""
import uuid
import redis
from functools import wraps
from typing import Union, Callable, Optional


def count_calls(method: Callable) -> Callable:
    """
        Increments the count for that key every
        time the method is called and returns
        the value returned by the original method.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
            Incerement.
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
        Store the history of inputs and outputs
        for the particular function.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """
            Wrapper Function.
        """
        self._redis.rpush('{}:inputs'.format(method.__qualname__), str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush('{}:outputs'.format(method.__qualname__), result)
        return result
    return wrapper


def replay(method: Callable):
    """
        Dispaly the history of calls of
        particular function.
    """
    rd = redis.Redis()

    method_name = method.__qualname__
    number_of_calls = rd.get(method_name).decode('utf-8')
    inputs_list = rd.lrange('{}:inputs'.format(method_name), 0, -1)
    outputs_list = rd.lrange('{}:outputs'.format(method_name), 0, -1)

    print("{} was called {} times:".format(method_name, number_of_calls))
    for i, o in zip(inputs_list, outputs_list):
        print("{}(*{}) -> {}".format(method_name, i.decode('utf-8'),
                                     o.decode('utf-8')))


class Cache:
    """
        Define Cache Class.
    """
    def __init__(self):
        """
            Constructor
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            Generate a random key store the input
            data in Redis using the random key
            and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
             take a key string argument and an Optional
             Callable argument named fn, and convert
             the data back to the desired format.
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
            Convert the data to string.
        """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """
            Convert the data to integer.
        """
        return self.get(key, int)
