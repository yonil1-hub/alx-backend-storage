#!/usr/bin/env python3
"""
List all documents in a collection
"""


def list_all(mongo_collection):
    """
    Return an empty list if no document in the collection
    else it returns the documents
    """
    documents = mongo_collection.find()
    return documents
