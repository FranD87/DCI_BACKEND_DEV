# First, execute the following command to create the file repository configuration:
# $ sudo sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list'
# Second, import the repository signing key:
# $ wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo apt-key add -
# Third, update the package list:
# $ sudo apt-get update
# Finally, install the latest version of PostgreSQL:
# $ sudo apt-get install postgresql
# set up password:
# sudo -u postgres psql
# \password
# check DB:
# postgres=# \l
# create the database using the CREATE DATABASE statement:
# postgres=# create database julia_dci-test;
# \c helloworld -> to connect to specific db
# create table:
# CREATE TABLE my_user (ID INT PRIMARY KEY NOT NULL, f_name TEXT NOT NULL, l_name TEXT NOT NULL);
# \d table name to view table details
# insert data in table:
# INSERT INTO my_user (ID, f_name, l_name) VALUES (3, 'Julia', 'Shcherbyna');
#  SELECT * FROM my_user;
# install DBeaver:
# sudo snap install dbeaver-ce
# create venv:
# python3.10 -m venv venv
# activate venv:
# source venv/bin/activate
# The \i file_name.sql command executes a file with instructions.
# \i test.sql




