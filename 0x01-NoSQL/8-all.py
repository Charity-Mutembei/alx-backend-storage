#!/usr/bin/env python3
"""
a Python function that lists all documents in a collection:
Prototype: def list_all(mongo_collection):
Return an empty list if no document in the collection
mongo_collection will be the pymongo collection object
"""


def list_all(mongo_collection):
    """
    Use find() to retrieve all documents in the collection
    """
    cursor = mongo_collection.find({})
    
    """
    Convert the cursor to a list of documents
    """
    documents = list(cursor)
    
    return documents
