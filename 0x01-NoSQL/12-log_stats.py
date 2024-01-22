#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 22-01-2024
"""
from pymongo import MongoClient


if __name__ == '__main__':
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    client = MongoClient('mongodb://127.0.0.1:27017')
    # get nginx collection
    nginx = client.logs.nginx
    logs = list(nginx.aggregate([
        {"$group": {"_id": "$method", "count": {"$sum": 1}}},
        {"$match": {"_id": {"$in": methods}}}
    ]))
    print("Methods:")
    for method in methods:
        log = next(filter(lambda x: x.get("_id") == method, logs), None)
        (print(f"\tmethod {method}: {log['count']}")
         if log else print(f"\tmethod {method}: 0"))
