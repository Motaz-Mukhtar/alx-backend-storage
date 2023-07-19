#!/usr/bin/env python3
"""
    Write function def schools_by_topic(mongo_collection, topic):
"""


def schools_by_topic(mongo_collection, topic):
    """
        Returns the list of school having a specific topic.
    """
    return mongo_collection.find({'topics': topic})
