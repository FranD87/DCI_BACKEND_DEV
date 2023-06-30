# CREATE TABLE employee_area (id SERIAL PRIMARY KEY, name VARCHAR (255), salary FLOAT);
# INSERT INTO employee_area (name, salary) VALUES ('Jhon Douh', 34987), ('Test emp', 2678), ('test 3', 983556);
# SELECT COUNT(salary), SUM(salary), AVG(salary), MIN(salary), MAX(salary) FROM employee_area;
# SELECT COUNT(*), COUNT(name), COUNT(DISTINCT name) FROM employee_area;
# INSERT INTO employee_area (name, salary) VALUES ('test null', NULL);
# avg(field_name) produces the average considering only those records that are not null on the field_name.
# SELECT AVG(salary), SUM(salary)::numeric/COUNT(*) FROM employee_area;
# SELECT COUNT (salary) FROM employee_area;
# Grouping records can also be tailored using the GROUP BY clause.
# SELECT city_id FROM area GROUP BY city_id;
# SELECT city_id FROM area;
# SELECT type from area GROUP BY type;
# SELECT name, city_id FROM area GROUP BY city_id; -> ERROR:  column "area.name" must appear in the GROUP BY clause or be used in an aggregate function
# SELECT city_id, COUNT(name) FROM area GROUP BY city_id;
# ALTER TABLE employee_area ADD COLUMN type VARCHAR(255);
# UPDATE employee SET type = 'Accounter';
# UPDATE employee SET type = 'GM' WHERE id = 1;
# SELECT type, AVG(salary) FROM employee GROUP BY type;


