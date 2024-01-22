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
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
