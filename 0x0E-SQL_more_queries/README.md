## SQL round two
---

## Granting permissions and creating new users.
* Creating a new user
	`CREATE USER 'username'@'host' IDENTIFIED WITH 'authentication_plugin' BY 'password';
	- for 'localhost' usage aka only on your machine
	- 'auth_socket' which will require user password each time acessing a database
	- down side prevents remote access privileges.
	- not necessary to be parsed for default mysql 'caching_sha2_password' to take effect
	`CREATE USER 'tommy'@'localhost' IDENTIFIED BY 'password';
	- this is a simple demonstration of how to create a new user Normally.
	- creating user while using the older framework such as PHP you will need to use 'mysql_native_password'
* Chaning the new user privileges
	- If you want to change some values in the user tables you can use the 'ALTER' keyword which will just make all the changes you want to take effect
	'ALTER USER 'tommy'@'localhost' IDENTIFIED WITH mysql_native_password' BY 'password';

* Granting a User Permission
	'grant 'privilege' on 'database.table' to 'username'@'host';
	- passing all privileges globally on the server you can use the `*`
	- for specific permission you can list them out all sep by commas
	'GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'sammy'@'localhost' WITH GRANT OPTION;'
	- 'FLUSH PRIVILEGES'
	- this will alter all the changes that you will need to make changes.
	- Remove all the granted permission to a particular user
		'REVOKE 'type_of_permission' ON 'database_name'.'table_name' FROM 'username'@'host';
	- List all the permission granted to the user.
		'SHOW GRANTS FOR 'username'@'hosts';
	- Deleting user database
		'DROP USER 'usernam'@'host';

* Constrains
	- what are the limits to enforce on either the tabel or the columns.
	- NOT NULL, UNIQUE, PRIMARY KEY FOREIGN KEY, ENUM and SET


### NOT NULL
- All the table and columns in the database table and column needs to be filled with values and no NULL values
	`CREATE TABLE first_table (id INT(11) NOT NULL, name VARCHAR(256) NOT NULL);`
	`INSERT INTO first_table VALUES(1, 'hello_world');
	fail..
	'INSERT INTO fist_table VALUES(2, NULL);

### UNIQUE
- Only allow column values that are unique meaning no repetition of the same values over and over again.
	`CREATE TABLE first_table (id INT(11) NOT NULL, name VARCHAR(256) UNIQUE);`
	`INSERT INTO first_table VALUES(1, 'coffee');
	`INSERT INTO first_table VALUES(1, 'cake');
	fail..{ERROR 1062 (23000): Duplicate entry 'cake' for key 'name'}
	`INSERT INTO first_table VALUES(1, 'cake');

- PRIMARY KEY have bultin in UNIQUE enbeded inside of them.

