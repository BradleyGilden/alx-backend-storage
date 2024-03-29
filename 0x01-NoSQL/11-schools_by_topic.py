#!/usr/bin/env python3

"""
<module docstring>

Author: Bradley Dillion Gilden
Date: 22-01-2024
"""
from pymongo import MongoClient


def schools_by_topic(mongo_collection, topic):
    """filters school docs by topic"""
    return list(mongo_collection.find({"topics": {"$in": [topic]}}))


if __name__ == "__main__":
    list_all = __import__("8-all").list_all
    insert_school = __import__("9-insert_school").insert_school
    client = MongoClient("mongodb://127.0.0.1:27017")
    school_collection = client.my_db.school

    j_schools = [
        {
            "name": "Holberton school",
            "topics": ["Algo", "C", "Python", "React"],
        },
        {"name": "UCSF", "topics": ["Algo", "MongoDB"]},
        {"name": "UCLA", "topics": ["C", "Python"]},
        {"name": "UCSD", "topics": ["Cassandra"]},
        {"name": "Stanford", "topics": ["C", "React", "Javascript"]},
    ]
    for j_school in j_schools:
        insert_school(school_collection, **j_school)

    schools = schools_by_topic(school_collection, "Python")
    for school in schools:
        print(
            "[{}] {} {}".format(
                school.get("_id"), school.get("name"), school.get("topics", "")
            )
        )
