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
* [2-fans.sql](2-fans.sql) - ranks country origins of bands, ordered by the number of (non-unique) fans
* [3-glam_rock.sql](3-glam_rock.sql) - lists all bands with Glam rock as their main style, ranked by their longevity
* [4-store.sql](4-store.sql) - a SQL script that creates a trigger that decreases the quantity of an item after adding a new order.
* [5-valid_email.sql](5-valid_email.sql) - a SQL script that creates a trigger that resets the attribute valid_email only when the email has been changed
* [6-bonus.sql](6-bonus.sql) - a SQL script that creates a stored procedure AddBonus that adds a new correction for a student.
* [7-average_score.sql](7-average_score.sql) - a SQL script that creates a stored procedure ComputeAverageScoreForUser that computes and store the average score for a student. Note: An average score can be a decimal
* [8-index_my_names.sql](8-index_my_names.sql) - a SQL script that creates an index idx_name_first on the table names and the first letter of name
* [9-index_name_score.sql](9-index_name_score.sql) - a SQL script that creates an index idx_name_first_score on the table names and the first letter of name and the score
* [10-div.sql](10-div.sql) - a SQL script that creates a function SafeDiv that divides (and returns) the first by the second number or returns 0 if the second number is equal to 0
* [11-need_meeting.sql](11-need_meeting.sql) - a SQL script that creates a view need_meeting that lists all students that have a score under 80 (strict) and no last_meeting or more than 1 month.
* []() - 
* []() - 
