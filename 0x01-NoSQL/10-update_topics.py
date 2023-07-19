#!/usr/bin/env python3
"""
    Write a function def update_topics(mongo_collection, name, topics):
"""
from pymongo.collection import Collection
from typing import List


def update_topics(mongo_collection: Collection, name: str,
                  topics: List[str]) -> None:
    """
        Change all topics of a school document based on the name.
    """
    mongo_collection.update_many({'name': name}, {'$set': {'topics': topics}})
