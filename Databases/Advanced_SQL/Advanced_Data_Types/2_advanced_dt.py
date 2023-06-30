# Create first table
# CREATE TABLE country (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL);
# INSERT INTO country (name) VALUES ('Germany'), ('France'), ('USA');
# create 2 table
# CREATE TABLE city (id SERIAL PRIMARY KEY, name VARCHAR(255), country_id INT REFERENCES country);
# INSERT INTO city (name, country_id) VALUES ('Berlin', 1), ('Marseille', 2), ('Rome', 2), ('Chicago', 3);
# # CREATE TABLE area (id SERIAL PRIMARY KEY, name VARCHAR(255), city_id INT REFERENCES city);
# # INSERT INTO area (name, city_id) VALUES ('location A', 2), ('location B', 5), ('location C', 2), ('location D', 3), ('location E', 1);
# Enumerated Types
# Types of data that comprise an ordered set of values.
# CREATE TYPE location_type AS ENUM('Selling point', 'Local office', 'Headquarters');
# ALTER TABLE area ADD COLUMN type location_type;
# UPDATE area SET type = 'Something else'; -> ERROR
# UPDATE area SET type = 'SELLING POINT'; -> ERROR
# UPDATE area SET type = 'Local office';
# UPDATE area SET type = 'Headquarters' WHERE name = 'location A';
# UPDATE area SET type = 'Selling point' WHERE name = 'location D';
# SELECT * FROM area ORDER BY type;
# SELECT * FROM area WHERE type > 'Selling point';
# UUID
# Universally Unique Identifiers
# SELECT * FROM pg_extension;
# CREATE EXTENSION "uuid-ossp";
# SELECT * FROM pg_extension;
# SELECT uuid_generate_v4();
# CREATE TABLE user_test (user_uuid uuid DEFAULT uuid_generate_v4(), name VARCHAR(255) NOT NULL, PRIMARY KEY (user_uuid));
# INSERT INTO user_test (name) VALUES ('JULIA'), ('Anna');
# SELECT * FROM user_test;
# JSON Types
# JavaScript Object Notation
# ALTER TABLE area ADD COLUMN info JSON;
# UPDATE area SET info='{"general": "TRUE", "some_extra_information": "bla-bla-bla"}';
# {field} -> {key} -> Returns a JSON data type.
# {field} ->> {key} -> Returns a text data type.
# SELECT info->'general', pg_typeof(info->'general'), info->>'general', pg_typeof(info->>'general') FROM area WHERE info->>'general'='TRUE';
# Querying: nested JSON paths
# {field} #> {key} -> Returns a JSON data type.
# {field} #>> {key} -> Returns a text data type
# UPDATE area SET info = '{"all": {"ok": true}}' WHERE type = 'Headquarters';
# SELECT info#>'{all,ok}', pg_typeof(info#>'{all,ok}'), info#>>'{all,ok}', pg_typeof(info#>>'{all,ok}') FROM area WHERE info#>>'{all,ok}' = 'true';
# The type jsonb is very similar to the type json but it is stored in binary form.
# Advantages over the json type:
# more efficient,
# significantly faster to process,
# supports indexing.
# ALTER TABLE area ADD COLUMN infob jsonb;
# UPDATE area SET infob = '{"all": "ok", "none": 2}' WHERE type = 'Headquarters';
# {json} @> {json} -> Returns True if the left JSON includes the right JSON.
# {json} <@ {json} -> Returns True if the right JSON includes the left JSON.
# SELECT name, infob, infob@>'{"all": "ok"}' FROM area;
# {jsonb} ? {key} -> Returns True if the left JSON has a key with the name key.
# SELECT name, infob, infob?'all', infob?'something' FROM area;
# Array Types
# A field can be defined as an array of any other data type.
# ALTER TABLE area
# ADD COLUMN q_earnings integer[];
# ALTER TABLE area
# ADD COLUMN alternate_name varchar[];
# ALTER TABLE area
# ADD COLUMN boundaries jsonb[];
# Indexing of array in SQL starts from 1 NOT 0
# UPDATE area SET q_earnings = ARRAY[0, 0, 0, 0];
# UPDATE area SET q_earnings = ARRAY[10, 14, 19, 13] WHERE type = 'Headquarters';
# SELECT name, type, q_earnings[1] AS Q1, q_earnings[2] AS Q2 FROM area WHERE q_earnings[2] > 10;
# ALTER TABLE area ADD COLUMN opened INTEGER [][];
# UPDATE area SET opened = ARRAY[[8, 12], [13, 17]];
# UPDATE area SET opened [2][2] = 19 WHERE type = 'Headquarters';
# UPDATE area SET  q_earnings = array_append(q_earnings, 100);
# UPDATE area SET q_earnings = array_remove(q_earnings, 100) WHERE type = 'Headquarters';
# SELECT * FROM area WHERE array_length(q_earnings, 1) > 4;
# DATETIME
# ALTER TABLE area ADD COLUMN opened_date date;
# UPDATE area SET opened_date = ‘1999-01-23’;
# ALTER TABLE area ADD COLUMN opened_time TIME;
# UPDATE area SET opened_time = '15:23:59';
# ALTER TABLE area ADD COLUMN opened_ts TIMESTAMP;
# UPDATE area SET opened_ts = '2004-10-19 10:23:54';
# SELECT CURRENT_TIMESTAMP - opened_ts AS "Days open" FROM area;









