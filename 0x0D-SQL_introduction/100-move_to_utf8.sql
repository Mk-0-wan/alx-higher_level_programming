-- Moving all your database to utf8 encoding
DROP DATABASE IF EXISTS hbtn_0c_0;
CREATE DATABASE IF NOT EXISTS hbtn_0c_0 CHARSET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE TABLE IF NOT EXISTS first_table ( id INT(11), name VARCHAR(256) );
