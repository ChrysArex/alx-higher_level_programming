-- script that creates the database hbtn_0d_2 and the user user_0d_2
-- creates the database hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creates the user user_0d_2
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
-- Grants the SELECT privilege in the database hbtn_0d_2 to user_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
