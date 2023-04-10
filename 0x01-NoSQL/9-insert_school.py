#!/usr/bin/env python3
"""
Insert a new document in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """
    Returns the new _id of created document
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
