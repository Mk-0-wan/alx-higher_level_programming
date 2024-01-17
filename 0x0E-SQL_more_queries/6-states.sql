-- Create a database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Create table from the database created above
CREATE TABLE IF NOT EXISTS states (
       	id INT PRIMARY KEY AUTO_INCREMENT,
       	name VARCHAR(256) NOT NULL
);
