-- Granting all permission to the new created USER
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES *.* TO 'user_0d_1'@'localhost';