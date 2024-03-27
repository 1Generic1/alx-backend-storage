#!/usr/bin/env python3
"""
    Returns the list of schools having a specific topic.
"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.
    """
    cursor = mongo_collection.find({"topics": topic})
    schools = list(cursor)
    return schools
