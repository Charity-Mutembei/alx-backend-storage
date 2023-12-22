#!/usr/bin/env python3
"""
a Python function that returns the list of
school having a specific topic:

Prototype: def schools_by_topic(mongo_collection, topic):
mongo_collection will be the pymongo collection object
topic (string) will be topic searched
"""


def schools_by_topic(mongo_collection, topic):
    """
    Use find to retrieve documents that match the given topic
    """
    cursor = mongo_collection.find({'topics': topic})
    
    """
    Convert the cursor to a list of schools
    """
    schools = list(cursor)
    
    return schools
