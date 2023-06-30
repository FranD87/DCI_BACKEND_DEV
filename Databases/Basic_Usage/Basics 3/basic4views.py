# CREATE VIEW friend_messages AS SELECT users.username, massage_1.massage FROM users, massage_1 WHERE users.id = massage_1.user_id;
# SELECT * FROM friend_messages;
# INSERT INTO massage_1 (massage, user_id) VALUES ('test massage', 3), ('test massage 2', 3), ('test massage5', 2);
# SELECT * FROM friend_messages WHERE massage LIKE '%e';
# ALTER VIEW IF EXISTS friend_messages RENAME TO full_name_messages;
# DROP VIEW IF EXISTS full_name_messages;
# CREATE OR REPLACE VIEW friend_messages AS SELECT users.username, massage_1.massage FROM users, massage_1 WHERE users.id = massage_1.user_id;
# CREATE TABLE friends (ID serial PRIMARY KEY NOT NULL, name varchar(255) NOT NULL, age integer);
# INSERT INTO friends (name, age) VALUES ('Alex', 21), ('Misha', 13), ('Tom', 17), ('Greg', 7), ('Monica', 19);
# CREATE OR REPLACE VIEW teenage_friends AS SELECT friends.name, friends.age FROM friends WHERE friends.age BETWEEN 13 AND 19;
# SELECT * FROM teenage_friends;
# INSERT INTO teenage_friends (name, age) VALUES ('Amina', 27); -> will insert to table friends
# SELECT * FROM teenage_friends;
# SELECT * FROM friends;
# Adding WITH CHECK OPTION will require the inserted values to match the conditions in the query defined in the view.
# CREATE OR REPLACE VIEW teenage_friends AS SELECT friends.name, friends.age FROM friends WHERE friends.age BETWEEN 13 AND 19 WITH CHECK OPTION;
# INSERT INTO teenage_friends (name, age) VALUES ('Anna', 26); -> ERROR:  new row violates check option for view
# "teenage_friends"

# CREATE MATERIALIZED VIEW teen_frnd AS SELECT friends.name, friends.age FROM friends WHERE friends.age BETWEEN 13 AND 19;
# SELECT * FROM teen_frnd;
# INSERT INTO teen_frnd (name, age) VALUES ('Amin', 17); -> ERROR:  cannot change materialized view "teen_frnd"
# INSERT INTO friends (name, age) VALUES ('Amin', 17);
# REFRESH MATERIALIZED VIEW teen_frnd;
# SELECT * FROM teen_frnd;
# This kind of view is useful when the query takes long to execute. It may be used as a cache of the results.
# Then, there is usually a logic that will refresh the materialized view when changes are made or in a periodical way.
# This way, the expensive calculations are only done when needed (when the data changes), instead of doing them every
# time we want to observe that information.
# A materialized view is a view that has been made persistent by storing its results in a temporary table.
# Subsequent calls to the view, will not process the underlying query, but will return the previously stored data.
# The query will not be executed unless the materialized view is refreshed (re-evaluated).
