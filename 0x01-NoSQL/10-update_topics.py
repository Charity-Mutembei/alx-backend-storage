#!/usr/bin/env python3
"""
a Python function that changes all topics of a
school document based on the name:

Prototype: def update_topics(mongo_collection, name, topics):
mongo_collection will be the pymongo collection object
name (string) will be the school name to update
topics (list of strings) will be the list of topics
approached in the school
"""


def update_topics(mongo_collection, name, topics):
    """
    Use update_many to update documents that
    match the given name
    """
    result = mongo_collection.update_many({'name': name},
                                          {'$set': {'topics': topics}})
    
    """
    Return the number of documents modified
    """
    return result.modified_count
