#!/usr/bin/env python3
"""
    Task 101
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score.
    The average score is included in each item returned
    with key 'averageScore'.
    """
    pipeline = [
        {
            '$addFields': {
                'averageScore': {'$avg': '$scores.score'}
            }
        },
        {
            '$sort': {
                'averageScore': -1
            }
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
