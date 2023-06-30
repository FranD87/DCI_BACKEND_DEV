
# Keys
# CREATE TABLE users (ID serial PRIMARY KEY NOT NULL, username varchar(255) NOT NULL);
# INSERT INTO users (username) VALUES ('mamasitta'), ('new_user'), ('Some new user');
# CREATE TABLE massage (ID serial PRIMARY KEY NOT NULL, massage TEXT NOT NULL, user_id INT REFERENCES users);
# INSERT INTO massage (massage, user_id) VALUES ('test massage', 1), ('test massage 2', 1), ('test massage3', 2);
# INSERT INTO massage (massage, user_id) VALUES ('test massage 4', 10); -> ERROR
# SELECT users.username, massage.massage FROM users, massage WHERE users.ID = massage.user_id;
# what will happened when we will try to delete from users?
# DELETE FROM users WHERE ID=1;
# The two most common modes for ON DELETE are SET NULL and CASCADE.
# SET NULL will set the referencing value to NULL.
# CASCADE will delete the referencing row.
# CREATE TABLE massage_1 (ID serial PRIMARY KEY NOT NULL, massage TEXT NOT NULL, user_id INT REFERENCES users ON DELETE SET NULL);
# INSERT INTO massage_1 (massage, user_id) VALUES ('test massage', 1), ('test massage 2', 1), ('test massage3', 2);
# CREATE TABLE massage_2 (ID serial PRIMARY KEY NOT NULL, massage TEXT NOT NULL, user_id INT REFERENCES users ON DELETE CASCADE);
# INSERT INTO massage_2 (massage, user_id) VALUES ('test massage', 1), ('test massage 2', 1), ('test massage3', 2);
# DELETE FROM massage WHERE user_id IN (1, 2);
# DELETE FROM users WHERE ID=1;
# SELECT * FROM massage_2;
# SELECT * FROM massage_1;




