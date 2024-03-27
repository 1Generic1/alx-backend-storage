#!/usr/bin/env python3
"""
    Inserts a new document into a MongoDB
    collection based on provided keyword arguments.
"""
def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document into a MongoDB
    collection based on provided keyword arguments.
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
