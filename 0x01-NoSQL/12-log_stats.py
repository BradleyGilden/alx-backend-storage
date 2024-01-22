#!/usr/bin/env python3
"""
if __name__ == "__main__":
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    client = MongoClient("mongodb://127.0.0.1:27017")
    # get nginx collection
    nginx = client.logs.nginx
    logs = list(
        nginx.aggregate(
            [
                {"$group": {"_id": "$method", "count": {"$sum": 1}}},
                {"$match": {"_id": {"$in": methods}}},
            ]
        )
    )
    print("Methods:")
    for method in methods:
        log = next(filter(lambda x: x.get("_id") == method, logs), None)
        (
            print(f"\tmethod {method}: {log['count']}")
            if log
            else print(f"\tmethod {method}: 0")
        )
"""
from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection, option=None):
    """
    Prototype: def log_stats(mongo_collection, option=None):
    Provide some stats about Nginx logs stored in MongoDB
    """
    items = {}
    if option:
        value = mongo_collection.count_documents(
            {"method": {"$regex": option}})
        print(f"\tmethod {option}: {value}")
        return

    result = mongo_collection.count_documents(items)
    print(f"{result} logs")
    print("Methods:")
    for method in METHODS:
        log_stats(nginx_collection, method)
    status_check = mongo_collection.count_documents({"path": "/status"})
    print(f"{status_check} status check")


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_collection)
