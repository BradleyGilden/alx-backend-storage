# MYSQL - Advanced

This directory will cover advanced mysql topics that were not covered previously in the course

***N.B sql scripts are run on MySQL v5.7 using an Ubuntu 18.04 LTS environment***

## General Objectives

* How to create tables with constraints
* How to optimize queries by adding indexes
* What is and how to implement stored procedures and functions in MySQL
* What is and how to implement views in MySQL
* What is and how to implement triggers in MySQL

## Tasks

* [0-uniq_users.sql](0-uniq_users.sql) - Write a SQL script that creates a table users following these requirements:
  * id, integer, never null, auto increment and primary key
  * email, string (255 characters), never null and unique
  * name, string (255 characters)<br>
  If the table already exists, your script should not fail
  Your script can be executed on any database
* [1-country_users.sql](1-country_users.sql) - Write a SQL script that creates a table users following these requirements:
  * id, integer, never null, auto increment and primary key
  * email, string (255 characters), never null and unique
  * name, string (255 characters)
  * country, enumeration of countries: US, CO and TN, never null (= default will be the first element of the enumeration, here US)<br>
  If the table already exists, your script should not fail
  Your script can be executed on any database
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
* []() - 
