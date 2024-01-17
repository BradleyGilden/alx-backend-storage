-- Make an attribute unique directly in the table schema

-- Creating Table
CREATE TABLE IF NOT EXISTS users (
    id AUTO_INCREMENT NOT NULL PRIMARY KEY,
    email VARCHAR(255) NOT NULL UNIQUE,
    name VARCHAR(255)
);
