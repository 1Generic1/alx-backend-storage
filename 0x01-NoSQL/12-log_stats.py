#!/usr/bin/env python3
"""
   this script Analyzes Nginx logs stored in a MongoDB collection and provides statistics.
"""


def nginx_logs_stats():
    """
   this script Analyzes Nginx logs stored in a MongoDB collection and provides statistics.
    """
    client = MongoClient('localhost', 27017)
    db = client['logs']
    collection = db['nginx']
    total_logs = collection.count_documents({})
    method_counts = {"GET": 0, "POST": 0, "PUT": 0, "PATCH": 0, "DELETE": 0}
    for doc in collection.find({}, {"_id": 0, "method": 1}):
        method = doc["method"]
        if method in method_counts:
            method_counts[method] += 1
    print("\tMethods:")
    for method, count in method_counts.items():
        print(f"\t\t{count} {method}")
    count_status = collection.count_documents({"method": "GET", "path": "/status"})
