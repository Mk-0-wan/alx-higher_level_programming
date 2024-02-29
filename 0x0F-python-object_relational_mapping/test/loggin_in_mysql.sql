-- Creates a password according to what you have set over here
ALTER USER 'root'@'localhost' IDENTIFIED WITH caching_sha2_password BY 'mypass12141214';
FLUSH PRIVILEGES;
exit;

