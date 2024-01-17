-- Make an attribute unique directly in the table schema
-- Ensure database exists
CREATE DATABASE IF NOT EXISTS holberton;
-- Creating Table
CREATE TABLE IF NOT EXISTS holberton.users (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
