#!/usr/bin/env python3
"""
    Redis Client
"""
import uuid
import redis
from typing import Union


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

    def store(self, data: Union[str, float, bytes, int]) -> str:
        """
            Generate a random key store the input
            data in Redis using the random key
            and return the key.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
