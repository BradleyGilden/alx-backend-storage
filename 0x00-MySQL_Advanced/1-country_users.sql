-- create a table with an enumeration

-- drop previous user table if exists
DROP TABLE IF EXISTS holberton.users;

-- create new user table with enum
CREATE TABLE IF NOT EXISTS holberton.users (
    id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255),
    country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
);
