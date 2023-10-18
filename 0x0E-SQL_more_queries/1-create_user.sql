-- script that creates the MySQL server user user_0d_1
-- If the user user_0d_1 already exists, the script not fail
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
-- adding the privileges
GRANT ALL PRIVILEGES ON *.*  TO 'user_0d_1'@'localhost';
