#!/usr/bin/env python3
"""
a Python function that returns
all students sorted by average score:
"""


def top_students(mongo_collection):
    """
    Use aggregate to calculate the average score for each student
    """

    pipeline = [
        {
            '$group': {
                '_id': '$student_id',
                'averageScore': {'$avg': '$score'}
            }
        },
        {
            '$sort': {'averageScore': -1}
        }
    ]

    """
    Execute the aggregation pipeline
    """
    result = mongo_collection.aggregate(pipeline)

    """
    Convert the cursor to a list of top students with average scores
    """
    top_students_list = list(result)

    return top_students_list
