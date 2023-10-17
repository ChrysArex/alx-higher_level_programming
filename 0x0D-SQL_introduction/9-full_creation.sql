-- script that creates a table second_table in the database hbtn_0c_0
-- Commande to create the table 'second_table'
CREATE TABLE IF NOT EXISTS second_table (
  id INT,
  name VARCHAR(256),
  score INT
);
-- Commande to insert the data
INSERT INTO second_table VALUES 
  (1, "John", 10),
  (2, "Alex", 3),
  (3, "Bob", 14),
  (4, "George", 8);
