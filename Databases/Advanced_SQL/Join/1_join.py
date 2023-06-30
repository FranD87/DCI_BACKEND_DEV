# Create first table
# CREATE TABLE country (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL);
# INSERT INTO country (name) VALUES ('Germany'), ('France'), ('USA');
# create 2 table
# CREATE TABLE city (id SERIAL PRIMARY KEY, name VARCHAR(255), country_id INT REFERENCES country);
# INSERT INTO city (name, country_id) VALUES ('Berlin', 1), ('Marseille', 2), ('Rome', 2), ('Chicago', 3);
# join 2 tables
# SELECT * FROM city JOIN country ON country.id = city.country_id;
# join with changing column names
# SELECT country.name AS "Country", city.name AS "City" FROM city JOIN country ON country.id = city.country_id;
# create new column in table city
# ALTER TABLE city
# ADD COLUMN city VARCHAR(255);
# Fill new column country in table city with referenced values
# UPDATE city SET country = Country.name FROM country WHERE city.country_id = country.id;
# SELECT * FROM city JOIN country ON country.id=city.country_id ORDER BY country.name;
#
# INSERT INTO city (name, country_id) VALUES ('New York', NULL);
# SELECT * FROM city LEFT JOIN country ON country.id=city.country_id;
# INSERT INTO country (name) VALUES ('Ukraine');
# SELECT * FROM city RIGHT JOIN country ON country.id=city.country_id;
# SELECT * FROM city FULL JOIN country ON country.id=city.country_id;
# SELECT * FROM city FULL JOIN country ON country.id=city.country_id WHERE country_id=2;
# CREATE TABLE area (id SERIAL PRIMARY KEY, name VARCHAR(255), city_id INT REFERENCES city);
# INSERT INTO area (name, city_id) VALUES ('location A', 2), ('location B', 5), ('location C', 2), ('location D', 3), ('location E', 1);
# SELECT * FROM city FULL JOIN country ON country.id=city.country_id FULL JOIN area ON city.id = area.city_id;
# SELECT area.name AS Location, city.name AS City, country.name AS Country FROM area JOIN city ON
# city.id = area.city_id JOIN country ON country.id = city.country_id WHERE country.name = 'France';
#
#
#
#
#
#
#
#
#
#
#
#
