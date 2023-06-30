
# CREATE TABLE my_user (ID INT PRIMARY KEY NOT NULL, f_name TEXT NOT NULL, l_name TEXT NOT NULL, phone TEXT);
# \d my_user -> display table details
# \d+ my_user -> display more details about your table
# ALTER TABLE my_user -> is a command/clause used to modify/alter a table.
# ADD COLUMN address VARCHAR; -> add column to table
# ALTER TABLE my_user
# RENAME COLUMN address TO location; -> Rename column
# ALTER TABLE my_user
# ALTER location TYPE int;-> ERROR:  column "location" cannot be cast automatically to type integer
# HINT:  You might need to specify "USING location::integer".
# ALTER location TYPE int USING location::integer;
# ALTER TABLE my_user
# DROP location; -> remove column
# DROP TABLE my_user; -> drop table
# DROP DATABASE test_j; -> ERROR:  cannot drop the currently open database
# we need to change connection
# \c database name and then -> DROP DATABASE test_j;
# ALTER TABLE my_user DROP location; -> ERROR:  column "location" of relation "my_user" does not exist
# DROP TABLE my_user; -> ERROR:  table "my_user" does not exist
# DROP DATABASE test_j; -> database "test_j" does not exist
# To not get an errors we can add IF EXIST statement
# ALTER TABLE my_user DROP IF EXISTS location;
# DROP TABLE IF EXISTS my_user;
# DROP DATABASE IF EXISTS test_j;
# CREATE TABLE my_user (ID INT PRIMARY KEY NOT NULL, f_name TEXT NOT NULL, l_name TEXT NOT NULL, phone TEXT);
# INSERT INTO my_user VALUES (1, 'Julia', 'Shcherbyna', '0501853456');
# insert data in some fields:
# INSERT INTO my_user (ID, f_name, l_name) VALUES (2, 'Julia', 'Shcherbyna');
# We can insert multiple values:
# INSERT INTO my_user (ID, f_name, l_name) VALUES (3, 'Julia', 'Shcherbyna'), (4, 'Olga', 'Shcherbyna');
# SELECT * from my_user;
# SELECT f_name FROM my_user;
# elect with condition:
# SELECT f_name FROM my_user WHERE f_name='Julia';
# UPDATE table values:
# UPDATE my_user SET phone = '0000';
# update with conditions:
# UPDATE my_user SET f_name='Ola', l_name='Tsimbal' WHERE ID=2;
# DELETE FROM my_user; -> delete all rows in table
# TRUNCATE my_user; -> clear all rows in table (can be used for multiple tables coma separated)
# DELETE FROM my_user WHERE ID=3;
# INSERT INTO my_user (ID, f_name, l_name) VALUES (6, 'Julia', 'Shcherbyna'), (5, 'Olga', 'Shcherbyna');
# SELECT DISTINCT f_name FROM my_user; -> unique values
# SELECT f_name AS "Name", l_name AS "Family name" FROM my_user;
# SELECT f_name FROM my_user LIMIT 4;
# The OFFSET clause will omit the first <number> of rows in the output.
# SELECT ID, f_name, l_name FROM my_user OFFSET 2;
# INSERT INTO my_user (ID, f_name, l_name) VALUES (10, 'Zac', 'Adams');
# The ORDER BY clause can be used to sort the results.
# An additional clause can be used to define the direction of the sorting: ASCending or DESCending.
# If this clause is not define, it will be sorted ascendingly.
# SELECT ID, f_name, l_name FROM my_user ORDER BY f_name ASC;
# INSERT INTO my_user (ID, f_name, l_name) VALUES (11, 'Zac', 'Test');
# INSERT INTO my_user (ID, f_name, l_name) VALUES (3, 'Zac', 'Barry');
# SELECT ID, f_name, l_name FROM my_user ORDER BY f_name ASC, l_name ASC;

# CREATE TABLE students (ID INT PRIMARY KEY NOT NULL, f_name TEXT NOT NULL, l_name TEXT NOT NULL, age INT NOT NULL);
# INSERT INTO students (ID, f_name, l_name, age) VALUES (1, 'Zac', 'Barry', 21), (2, 'Julia', 'shcherbyna', 50), (3, 'Bob', 'Bay', 37), (4, 'Zac', 'Barry', 10);
# 2 yongerstone:
# SELECT ID, f_name, age FROM students ORDER BY age LIMIT 2;
# 1 oldest:
# SELECT ID, f_name, age FROM students ORDER BY age DESC LIMIT 1;
# SQL LOGICAL:
# SELECT ID, f_name, age FROM students WHERE age IN (21, 10);
# SELECT ID, f_name, age FROM students WHERE age > 9 AND age < 36;
# SELECT ID, f_name, age FROM students WHERE age BETWEEN 9 AND 36;
# Text fields have an additional operator named LIKE, that is used to match against patterns.
# The LIKE operator uses the % symbol that matches against any number of characters.
# SELECT ID, f_name, age FROM students WHERE f_name LIKE 'Z%';


