#!/usr/bin/env python3
"""
a Python function that inserts a new document
in a collection based on kwargs:
Prototype: def insert_school(mongo_collection, **kwargs):
mongo_collection will be the pymongo collection object
Returns the new _id
"""


def insert_school(mongo_collection, **kwargs):
    """
    Use insert_one to insert a new document
    into the collection
    """
    result = mongo_collection.insert_one(kwargs)
    
    """
    Return the new _id
    """
    return result.inserted_id
