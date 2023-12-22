#!/usr/bin/env python3
"""
a Python script that provides some stats
about Nginx logs stored in MongoDB:
"""

from pymongo import MongoClient


def nginx_logs_stats():
    """
    Connect to MongoDB
    """
    client = MongoClient('mongodb://localhost:27017')
    db = client['logs']
    collection = db['nginx']

    """
    Get the total number of logs
    """
    total_logs = collection.count_documents({})

    """
    Display the total number of logs
    """
    print(f"{total_logs} logs")

    """
    Display methods statistics
    """
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = collection.count_documents({'method': method})
        print(f"\t{method}: {count} logs")

    """
    Display specific log statistics
    """
    status_count = collection.count_documents({'method': 'GET', 'path': '/status'})
    print(f"Method=GET, Path=/status: {status_count} logs")


if __name__ == "__main__":
    nginx_logs_stats()
