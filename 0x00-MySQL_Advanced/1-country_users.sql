-- create a table with an enumeration
-- drop previous user table if exists
CREATE TABLE IF NOT EXISTS users(
    id int NOT NULL PRIMARY KEY AUTO_INCREMENT,
    email varchar(255) NOT NULL UNIQUE,
    name varchar(255),
    country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
);
