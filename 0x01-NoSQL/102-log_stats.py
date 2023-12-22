#!/usr/bin/env python3
"""
Improve 12-log_stats.py by adding the top 10 of the most
present IPs in the collection nginx of the database logs:
"""

from pymongo import MongoClient


def log_stats():
    """
    Connect to MongoDB
    """
    client = MongoClient('mongodb://localhost:27017')
    db = client['logs']
    collection = db['nginx']

    """
    Display the total number of logs
    """
    total_logs = collection.count_documents({})
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

    """
    Display the top 10 most present IPs
    """
    top_ips_pipeline = [
        {
            '$group': {
                '_id': '$ip',
                'count': {'$sum': 1}
            }
        },
        {
            '$sort': {'count': -1}
        },
        {
            '$limit': 10
        }
    ]

    top_ips_result = collection.aggregate(top_ips_pipeline)

    print("Top 10 IPs:")
    for idx, ip_info in enumerate(top_ips_result, 1):
        print(f"\t{idx}. IP: {ip_info['_id']}, Count: {ip_info['count']}")


if __name__ == "__main__":
    log_stats()
