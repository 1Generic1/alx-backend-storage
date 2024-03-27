#!/usr/bin/env python3
"""
    Changes all topics of a school document based on the school name.
"""


def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the school name.
    """
    result = mongo_collection.update_many(
            {"name": name},
            {"$set": {"topics": topics}}
    )
    return result.modified_count
