#!/usr/bin/env python3
"""
    Lists all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """
    Lists all documents in a MongoDB collection.
    """
    all_documents = []
    cursor = mongo_collection.find({})
    for document in cursor:
        all_documents.append(document)
    return all_documents
