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

    top_student = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_student
