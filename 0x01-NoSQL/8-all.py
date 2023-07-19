#!/usr/bin/env python3
"""
    Write Function def list_all(mongo_collection)
"""
from typing import List
from pymongo.collection import Collection


def list_all(mongo_collection: Collection) -> List[dict]:
    """
        Lists all documents in a collection.
    """
    doc_lists = []
    for doc in mongo_collection.find():
        doc_lists.append(doc)

    return doc_lists
