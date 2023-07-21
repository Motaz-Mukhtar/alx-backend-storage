#!/usr/bin/env python3
"""
    Redis Client
"""
import uuid
import redis
from typing import Union, Callable, Optional


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

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
            Generate a random key store the input
            data in Redis using the random key
            and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable]=None) -> Union[str, bytes, int, float]:
        """
             take a key string argument and an Optional
             Callable argument named fn, and convert
             the data back to the desired format.
        """
        data = self._redis.get(key)

        if not data:
            return None
        
        return fn(data)
        

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
