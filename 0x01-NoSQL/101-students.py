#!/usr/bin/env python3

"""
Author: Bradley Dillion Gilden
Date: 22-01-2024
"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    """
    return mongo_collection.aggregate([
        {
            "$project":
            {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {
            "$sort":
            {
                "averageScore": -1
            }
        }
    ])
