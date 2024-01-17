-- Creating database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Creating a new user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Adding only SELECT privileges for the user_0d_1
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
-- Flush privileges to apply changes
FLUSH PRIVILEGES;
