# NoSQL - MongoDB

MongoDB is a NoSQL database (Not Only SQL). Data is not stored in tables and columns, instead related data are stored in a single document in field-value pairs (similar to JSON) e.g 

```JavaScript
{
    name: 'Bob',
    age: 32,
    gpa: 2.3,
    height: 6.1
}
```

## Learning Objectives

* What NoSQL means
* What is difference between SQL and NoSQL
* What is ACID
* What is a document storage
* What are NoSQL types
* What are benefits of a NoSQL database
* How to query information from a NoSQL database
* How to insert/update/delete information from a NoSQL database
* How to use MongoDB

## Tasks

* [0-list_databases](0-list_databases) - Write a script that lists all databases in MongoDB.
* [1-use_or_create_database](1-use_or_create_database) - Write a script that creates or uses the database my_db
* [2-insert](2-insert) - Write a script that inserts a document in the collection school:
  * The document must have one attribute name with value “Holberton school”
  * The database name will be passed as option of mongo command
* [3-all](3-all) - Write a script that lists all documents in the collection school
* [4-match](4-match) - Write a script that lists all documents with name="Holberton school" in the collection school
* [5-count](5-count) - Write a script that displays the number of documents in the collection school
* [6-update](6-update) - Write a script that adds a new attribute to a document in the collection school:
  * The script should update only document with name="Holberton school" (all of them)
  * The update should add the attribute address with the value “972 Mission street”
  * The database name will be passed as option of mongo command
* [7-delete](7-delete) - Write a script that deletes all documents with name="Holberton school" in the collection school
* [8-all](8-all) - Write a Python function that lists all documents in a collection
* [9-insert_school.py](9-insert_school.py) - a Python function that inserts a new document in a collection based on kwargs
* [10-update_topics.py](10-update_topics.py) - a Python function that changes all topics of a school document based on the name
* [11-schools_by_topic.py](11-schools_by_topic.py) - Write a Python function that returns the list of school having a specific topic
* [12-log_stats.py](12-log_stats.py) - Write a Python script that provides some stats about Nginx logs stored in MongoDB:
  * Database: logs
  * Collection: nginx
  * Display (same as the example):
    * first line: x logs where x is the number of documents in this collection
    * second line: Methods:
    * 5 lines with the number of documents with the method = `["GET", "POST", "PUT", "PATCH", "DELETE"]` in this order (see example below - warning: it’s a tabulation before each line)
    * one line with the number of documents with:
      * method=GET
      * path=/status
* []() - 
* []() - 
