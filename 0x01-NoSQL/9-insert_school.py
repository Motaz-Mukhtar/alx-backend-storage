#!/usr/bin/env python3
"""
    Write function def insert_school(mongo_collection, **kwargs):
"""
from pymongo.collection import Collection


def insert_school(mongo_collection: Collection, **kwargs: dict):
    """
        Inserts a new document in a collection
        based on kwargs
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
