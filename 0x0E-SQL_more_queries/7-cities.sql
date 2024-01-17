-- Create a database if it doesn't exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- Create table from the database created above
CREATE TABLE IF NOT EXISTS cities (
	id INT PRIMARY KEY AUTO_INCREMENT,
       	state_id INT NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id),
       	name VARCHAR(256) NOT NULL
);
