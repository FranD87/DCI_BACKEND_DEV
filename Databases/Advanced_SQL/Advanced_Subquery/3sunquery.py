
# SELECT inner_query."Location name" FROM (SELECT name AS "Location name", type AS "Location type", q_earnings AS "Earnings" FROM area) AS inner_query;
# CREATE TABLE test_subq (id INT PRIMARY KEY, name VARCHAR(255), city_id INT);
# INSERT INTO test_subq (id, name, city_id) VALUES (1, 'test1', 4), (2, 'test2', 1), (3, 'test3', 3);
# SELECT * FROM test_subq WHERE city_id NOT IN (SELECT id FROM city);
# SELECT name, (SELECT name FROM city WHERE city.id=test_subq.city_id) AS "City name" FROM test_subq;
# The EXISTS operator returns True if the subquery returns any rows and False otherwise.
# SELECT name, city_id, EXISTS (SELECT * FROM city WHERE id=test_subq.city_id) FROM test_subq;



