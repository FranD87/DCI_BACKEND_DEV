# CREATE TABLE account (id SERIAL PRIMARY KEY, name VARCHAR(255) NOT NULL, balance INT NOT NULL);
# INSERT INTO account (name, balance) VALUES ('Julia', 50000), ('Marcus', 55000), ('Pablo', 70000);
# INSERT INTO account (name, balance) VALUES ('Julia', 50000), ('Marcus', 55000), ('Pablo', 70000);
# BEGIN; UPDATE account SET balance = balance - 100 WHERE name='Julia'; SAVEPOINT julia_updated; UPDATE account SET
# balance =  balance + 100 WHERE name='Pablo'; ROLLBACK TO julia_updated; COMMIT;
# BEGIN; LOCK TABLE account; SELECT pg_sleep(10);COMMIT;
# BEGIN; LOCK TABLE account; SELECT pg_sleep(10);
# SELECT * FROM account; -> in other terminal
# till DB will not be committed no execution happened
#
#
#
