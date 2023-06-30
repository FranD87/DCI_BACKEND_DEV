CREATE TYPE visibility AS ENUM (
  'Public',
  'Private'
);

CREATE TABLE teacher (
    id serial PRIMARY KEY,
    name varchar(100),
    city varchar(100)
);

CREATE TABLE webinar (
  id serial PRIMARY KEY,
  name varchar(200) NOT NULL,
  teacher_id integer,
  visibility visibility DEFAULT 'Public' NOT NULL,
  starts_on timestamp with time zone,
  ends_on timestamp with time zone,
  audience integer,
  FOREIGN KEY (teacher_id) REFERENCES teacher(id)
);

INSERT INTO teacher(name, city) VALUES
	('Camila Muller', 'Frankfurt'),
	('Gerald Müller', 'Adelaide'),
	('Naomi Martí', 'Bern'),
	('Gerald Perez', 'Xiamen'),
	('Araceli Lee', 'Leipzig'),
	('Ahmed Allen', 'Auckalnd'),
	('Bernhard Hunter', 'Roma'),
	('Olivia Ali', 'Toulouse'),
	('Marc Nguyen', 'Munich'),
	('Bernhard Moore', 'Tubingen'),
	('Loretta Young', 'Donetsk'),
	('Loretta Wilson', 'Dresden'),
	('Itziar Perez', 'San Marino'),
	('Itziar Williams', 'Budapest'),
	('Yussef Anniston', 'Los Angeles'),
	('Julia Griesebner', 'Madrid'),
	('Aaliyah Lewis', 'Melbourne'),
	('Loretta Nguyen', 'Berlin'),
	('Johann Sanhchez', 'Auckalnd'),
	('Gianna O''Connor', 'Johannesburg'),
	('Chloe Swcharzenegger', 'Auckalnd'),
	('Abdul Allen', 'Mildura'),
	('Araceli Wilson', 'Cardiff'),
	('Yussef Wright', 'Venice'),
	('Gianna O''Connor', 'Toulouse'),
	('Yussef Lee', 'Xiamen'),
	('William Smith', 'Auckalnd'),
	('Gerald Muller', 'Kiev'),
	('Chloe Hunter', 'Muscat'),
	('Amelia Lewis', 'Graz'),
	('Yussef Allen', 'Paris'),
	('Johann Hill', 'New York'),
	('Keith Swcharzenegger', 'Los Angeles'),
	('Oriol Müller', 'Venice'),
	('Noah O''Connor', 'Berlin'),
	('Marc Brown', 'Marseille'),
	('Bernhard Johnson', 'Dortmund'),
	('Abdul Wright', 'Brussels'),
	('Camila Miller', 'Frankfurt'),
	('Chloe Anniston', 'Graz'),
	('Ahmed Anniston', 'Antwerp'),
	('Keith Muller', 'Naples'),
	('David Anniston', 'San Marino'),
	('Penelope O''Connor', 'Prague'),
	('Zain Adams', 'Marseille'),
	('Aaliyah Miller', 'Cardiff'),
	('Grace McDonald', 'Bilbao'),
	('Layla Perez', 'New York'),
	('Ella Fiedler', 'Prague'),
	('Arnold Clark', 'Vancouver'),
	('Nikolas White', 'Graz'),
	('Benjamin Black', 'Vancouver'),
	('Lucas Swcharzenegger', 'San Marino'),
	('Oriol Clark', 'Metz'),
	('Itziar Hunter', 'Leipzig'),
	('Penelope Masferrer', 'Guangzhou'),
	('Benjamin Hunter', 'Seattle'),
	('Evelyn Hunter', 'Dublin'),
	('David Davis', 'Salzburg'),
	('Emma Müller', 'San Marino'),
	('Julia Miller', 'Viena'),
	('Emma Ahmas', 'Graz'),
	('Marc Adams', 'Ottawa'),
	('Yussef White', 'Auckalnd'),
	('Anna Müller', 'Kiev'),
	('Yussef Clark', 'Barcelona'),
	('Ahmed Lewis', 'New York'),
	('Yussef Miller', 'Munich'),
	('Loretta Masferrer', 'Bilbao'),
	('Nikolas Davis', 'Mildura'),
	('Yamileth Hutticher', 'Roma'),
	('Yussef Young', 'Moscow'),
	('Grace Smith', 'Moscow'),
	('Johann Muller', 'Chicago'),
	('Yussef Vidal', 'Xiamen'),
	('Arturo Doe', 'Madrid'),
	('Emma Schumacher', 'Dresden'),
	('Gerald Vidal', 'Metz'),
	('Itziar Schumacher', 'Venice'),
	('Nikolas Young', 'Malmo'),
	('Anna Wright', 'Donetsk'),
	('Arturo Brown', 'San Diego'),
	('Arturo JAckson', 'Graz'),
	('Arturo Nguyen', 'Frankfurt'),
	('Yussef Ahmas', 'Leipzig'),
	('Johann White', 'Adelaide'),
	('Ella Garcia', 'Salzburg'),
	('Aarya Masferrer', 'Brussels'),
	('Araceli Young', 'Graz'),
	('Mia Müller', 'Antwerp'),
	('Layla Green', 'Malmo'),
	('Abdul Griesebner', 'Budapest'),
	('Abigail Young', 'Sydney'),
	('Itziar Lewis', 'Sheffield'),
	('Abdul Smith', 'Adelaide'),
	('Liam Martí', 'Seattle'),
	('Marc Young', 'Paris'),
	('Layla Davis', 'New York'),
	('Itziar Ahmas', 'Sarajevo'),
	('Camila Hill', 'Ottawa'),
	('Benjamin Smith', 'Sheffield'),
	('Ella O''Connor', 'Malmo'),
	('Arnold Griesebner', 'Sarajevo'),
	('Abigail Hunter', 'Paris'),
	('Zain Moore', 'Graz');
INSERT INTO webinar(name, teacher_id, visibility, starts_on, ends_on, audience) VALUES
	('Introduction to Django', 49, 'Public', '2018-01-25 16:05:20', '2018-01-25 07:03:58', 49),
	('Hands on Python', 91, 'Private', '2016-05-01 18:44:39', '2016-03-09 04:10:52', 32),
	('Hands on Python Algorithms', 91, 'Public', '2015-06-04 05:53:23', '2015-01-04 05:05:04', 10),
	('Hands on Python', 1, 'Private', '2020-10-01 04:03:36', '2020-04-21 08:46:15', 15),
	('Introduction to Python', 63, 'Private', '2008-03-01 03:48:24', '2008-02-18 06:29:27', 0),
	('Hands on Python Algorithms', 4, 'Private', '2016-07-03 15:02:47', '2016-06-26 05:51:19', 15),
	('Introduction to Python', 19, 'Public', '2021-05-18 06:33:23', '2021-03-10 13:32:21', 18),
	('Advanced Databases', 11, 'Public', '2007-07-09 07:23:16', '2007-01-24 23:37:24', 29),
	('Advanced Django Templates', 66, 'Private', '2019-08-29 14:05:11', '2019-07-23 14:27:45', 3),
	('Introduction to Django Templates', 45, 'Public', '2009-06-23 01:16:56', '2009-01-31 22:56:43', 1),
	('Introduction to Django Templates', 48, 'Public', '2011-07-06 21:19:48', '2011-06-19 06:05:53', 27),
	('Advanced Python Algorithms', 45, 'Private', '2016-04-26 20:03:23', '2016-04-23 09:52:35', 34),
	('Hands on Django Admin', 70, 'Private', '2016-07-28 22:00:40', '2016-06-02 15:44:34', 49),
	('Introduction to Databases', 70, 'Private', '2018-02-23 11:57:28', '2018-01-29 12:48:41', 6),
	('Advanced Python', 11, 'Private', '2017-11-29 18:58:05', '2017-09-04 10:40:09', 15),
	('Introduction to Python OOP', 45, 'Private', '2015-03-04 00:59:56', '2015-02-11 11:46:36', 39),
	('Introduction to Python Algorithms', 7, 'Public', '2011-06-24 15:09:22', '2011-01-27 12:17:57', 36),
	('Introduction to Django Templates', 80, 'Private', '2018-01-17 11:12:38', '2018-01-17 18:03:36', 10),
	('Advanced Django', 12, 'Private', '2019-06-10 10:01:29', '2019-04-07 08:07:00', 42),
	('Introduction to Computer', 54, 'Private', '2012-07-28 13:04:45', '2012-03-15 21:55:17', 1),
	('Advanced Python OOP', 35, 'Public', '2018-12-20 10:55:39', '2018-11-06 17:44:42', 19),
	('Hands on Django Templates', 36, 'Private', '2020-05-29 15:46:43', '2020-04-12 12:32:25', 14),
	('Advanced Python', 43, 'Private', '2015-12-09 09:59:16', '2015-07-25 20:52:29', 46),
	('Introduction to Python', 69, 'Private', '2021-05-17 22:53:13', '2021-04-01 17:42:32', 40),
	('Introduction to Computer', 12, 'Public', '2017-01-01 05:55:43', '2017-01-01 11:51:17', 15),
	('Hands on Python OOP', 12, 'Private', '2014-09-06 16:48:48', '2014-06-01 09:17:24', 42),
	('Introduction to Django Admin', 60, 'Public', '2016-01-03 11:03:54', '2016-01-03 05:32:22', 17),
	('Introduction to Python OOP', 9, 'Public', '2005-10-13 08:11:58', '2005-08-18 02:07:10', 9),
	('Hands on Django ORM', 98, 'Public', '2009-11-02 11:53:02', '2009-03-02 22:48:02', 28),
	('Advanced Databases', 64, 'Public', '2005-07-11 20:34:23', '2005-03-18 12:43:56', 7),
	('Introduction to Django Templates', 95, 'Private', '2019-06-28 20:26:54', '2019-02-24 06:29:20', 28),
	('Introduction to Django', 64, 'Private', '2008-12-07 07:52:13', '2008-01-11 05:52:01', 15),
	('Introduction to Django ORM', 65, 'Private', '2013-10-29 20:42:04', '2013-07-11 02:01:18', 46),
	('Advanced Python', 88, 'Private', '2011-08-04 02:50:05', '2011-07-16 22:25:33', 31),
	('Advanced Python OOP', 20, 'Private', '2010-04-28 03:26:13', '2010-04-22 16:42:06', 7),
	('Hands on Django Admin', 60, 'Private', '2005-09-01 07:14:09', '2005-06-02 08:59:44', 48),
	('Introduction to Python', 35, 'Public', '2006-05-24 17:56:32', '2006-03-25 17:17:42', 23),
	('Introduction to Databases', 33, 'Private', '2011-03-04 05:28:03', '2011-02-17 22:47:25', 21),
	('Hands on Django Admin', 39, 'Public', '2011-03-31 20:49:13', '2011-03-19 04:13:18', 44),
	('Hands on Python Algorithms', 70, 'Private', '2017-04-17 21:14:55', '2017-01-30 14:30:11', 31),
	('Introduction to Django Templates', 8, 'Public', '2007-10-09 00:31:38', '2007-08-18 22:46:12', 37),
	('Introduction to Django', 69, 'Private', '2011-01-02 13:47:57', '2011-01-02 06:58:09', 44),
	('Hands on Django Admin', 92, 'Public', '2018-06-16 15:59:43', '2018-05-22 11:43:39', 0),
	('Advanced Django', 87, 'Private', '2012-01-08 11:53:23', '2012-01-08 02:30:30', 44),
	('Advanced Django', 23, 'Public', '2007-12-07 04:01:11', '2007-06-11 10:07:09', 20),
	('Hands on Computer', 65, 'Private', '2019-12-01 13:07:26', '2019-10-22 17:07:57', 24),
	('Advanced Django', 28, 'Private', '2013-06-07 23:33:58', '2013-02-19 23:44:16', 18),
	('Advanced Python Algorithms', 63, 'Private', '2016-05-30 15:10:45', '2016-02-09 18:38:24', 27),
	('Advanced Computer', 12, 'Public', '2020-07-27 05:03:57', '2020-06-06 15:56:49', 13),
	('Advanced Computer', 48, 'Private', '2006-09-30 05:18:41', '2006-03-10 12:38:42', 43),
	('Hands on Django Admin', 26, 'Public', '2014-07-06 17:24:42', '2014-06-10 16:18:00', 20),
	('Advanced Django Templates', 8, 'Private', '2019-07-10 15:24:31', '2019-05-20 19:41:54', 2),
	('Advanced Computer', 19, 'Public', '2010-02-18 15:03:01', '2010-01-21 01:12:07', 9),
	('Hands on Python Algorithms', 61, 'Private', '2014-05-31 19:09:21', '2014-04-13 18:03:29', 41),
	('Advanced Django Templates', 4, 'Public', '2012-04-25 08:54:19', '2012-02-09 15:37:10', 49),
	('Advanced Django Templates', 51, 'Private', '2009-08-14 00:45:35', '2009-01-29 04:41:43', 41),
	('Advanced Databases', 22, 'Public', '2018-11-07 08:31:01', '2018-01-27 00:35:02', 8),
	('Introduction to Django', 99, 'Public', '2006-07-05 01:10:23', '2006-01-24 22:29:06', 7),
	('Hands on Python Algorithms', 2, 'Public', '2012-06-25 06:24:20', '2012-05-15 12:55:26', 15),
	('Hands on Python OOP', 67, 'Public', '2008-11-27 04:48:40', '2008-08-26 01:38:13', 10),
	('Hands on Python', 93, 'Public', '2009-12-31 21:26:24', '2009-05-05 08:22:03', 35),
	('Hands on Django Templates', 47, 'Private', '2008-02-22 03:14:38', '2008-02-08 06:06:57', 33),
	('Introduction to Python Algorithms', 43, 'Private', '2009-01-10 14:31:38', '2009-01-10 08:42:46', 21),
	('Hands on Django ORM', NULL, 'Private', '2014-08-30 13:25:55', '2014-08-21 20:57:03', 20),
	('Hands on Django Templates', 73, 'Public', '2017-10-05 02:58:11', '2017-01-26 11:01:15', 25),
	('Advanced Django', 82, 'Private', '2012-12-07 02:17:50', '2012-11-19 00:20:38', 34),
	('Hands on Computer', 29, 'Public', '2021-06-01 08:21:03', '2021-03-14 23:45:01', 47),
	('Introduction to Python', 9, 'Public', '2011-05-10 05:09:24', '2011-04-26 03:02:07', 7),
	('Hands on Databases', 47, 'Private', '2009-12-14 04:00:47', '2009-05-02 22:39:56', 27),
	('Advanced Django ORM', 45, 'Public', '2013-12-17 12:35:11', '2013-09-10 19:51:08', 12),
	('Hands on Python OOP', 43, 'Public', '2018-01-15 18:47:25', '2018-01-15 09:39:21', 15),
	('Introduction to Python Algorithms', 34, 'Private', '2007-05-21 23:07:04', '2007-05-04 16:34:59', 30),
	('Introduction to Django ORM', 42, 'Private', '2011-02-06 14:53:32', '2011-01-08 21:56:08', 3),
	('Advanced Computer', 28, 'Public', '2011-12-11 00:33:05', '2011-10-22 23:35:19', 31),
	('Introduction to Django Templates', 13, 'Public', '2019-07-30 03:58:31', '2019-05-30 02:18:58', 14),
	('Introduction to Python OOP', 25, 'Private', '2012-06-12 23:54:26', '2012-02-20 09:14:38', 9),
	('Advanced Python', 98, 'Private', '2020-01-27 16:54:53', '2020-01-27 20:39:48', 5),
	('Advanced Databases', 88, 'Private', '2008-07-26 16:38:37', '2008-07-11 14:54:55', 43),
	('Advanced Django', 94, 'Public', '2007-07-09 12:37:29', '2007-01-29 09:27:09', 20),
	('Hands on Django Templates', 11, 'Private', '2005-04-29 13:58:27', '2005-03-18 03:31:26', 1),
	('Hands on Python OOP', 85, 'Private', '2018-05-12 10:55:56', '2018-05-08 23:52:29', 34),
	('Advanced Django Templates', 75, 'Public', '2013-06-30 23:29:05', '2013-06-20 17:23:36', 1),
	('Advanced Django', 76, 'Private', '2020-05-05 03:01:59', '2020-03-29 09:50:55', 11),
	('Introduction to Databases', 104, 'Private', '2015-07-14 18:16:57', '2015-02-28 20:19:39', 28),
	('Advanced Django', 93, 'Public', '2009-11-29 09:38:26', '2009-03-10 07:14:51', 17),
	('Hands on Databases', 5, 'Private', '2009-07-07 01:26:40', '2009-03-09 06:40:23', 32),
	('Advanced Python', 15, 'Private', '2017-11-11 03:38:03', '2017-10-23 08:49:31', 32),
	('Introduction to Computer', 47, 'Public', '2010-04-04 18:03:19', '2010-01-29 04:06:22', 31),
	('Hands on Databases', 70, 'Private', '2010-09-06 18:34:00', '2010-01-30 11:22:17', 39),
	('Advanced Django Templates', 5, 'Private', '2017-09-03 15:54:00', '2017-07-12 19:37:39', 14),
	('Hands on Django', 8, 'Public', '2005-11-17 12:55:51', '2005-05-24 07:40:58', 20),
	('Hands on Computer', 30, 'Private', '2009-07-16 10:17:40', '2009-03-11 16:43:46', 11),
	('Advanced Python', 64, 'Private', '2007-10-09 21:09:19', '2007-01-27 05:41:24', 25),
	('Hands on Django', 39, 'Private', '2012-11-03 04:25:45', '2012-07-25 05:42:03', 39),
	('Introduction to Python Algorithms', 32, 'Private', '2013-05-01 00:14:31', '2013-04-06 05:11:15', 25),
	('Introduction to Django', 75, 'Public', '2013-12-18 15:53:45', '2013-04-17 21:23:35', 2),
	('Advanced Django Templates', 4, 'Private', '2019-12-20 16:39:20', '2019-11-12 03:16:03', 40),
	('Advanced Python OOP', 20, 'Private', '2009-12-01 19:30:59', '2009-08-12 00:48:42', 31),
	('Introduction to Python OOP', 13, 'Public', '2006-11-07 06:48:52', '2006-03-30 08:15:45', 14),
	('Hands on Django ORM', 86, 'Private', '2017-06-16 12:22:27', '2017-05-28 04:28:53', 46),
	('Advanced Python', 100, 'Public', '2020-04-06 12:29:28', '2020-04-02 06:10:04', 25),
	('Introduction to Django Admin', 77, 'Public', '2021-03-07 11:14:26', '2021-01-07 21:20:27', 42),
	('Introduction to Computer', 64, 'Private', '2016-12-07 17:59:18', '2016-01-08 20:00:02', 27),
	('Introduction to Django ORM', 12, 'Public', '2018-05-07 13:52:02', '2018-03-20 22:18:53', 22),
	('Hands on Django Admin', 36, 'Private', '2009-08-04 02:06:57', '2009-03-20 23:44:18', 31),
	('Introduction to Django ORM', NULL, 'Public', '2006-10-12 07:19:08', '2006-09-08 02:29:07', 16),
	('Advanced Python OOP', 91, 'Public', '2012-07-12 01:27:29', '2012-03-19 15:07:23', 1),
	('Introduction to Python', 66, 'Private', '2008-01-10 09:19:31', '2008-01-10 07:46:33', 24),
	('Introduction to Django Templates', 59, 'Public', '2009-04-25 13:57:13', '2009-03-21 10:39:45', 42),
	('Introduction to Computer', 63, 'Public', '2020-08-18 02:33:27', '2020-05-09 18:49:20', 18),
	('Advanced Databases', 95, 'Public', '2012-04-23 06:59:53', '2012-03-16 06:04:41', 6),
	('Hands on Python Algorithms', 76, 'Public', '2015-09-24 13:17:54', '2015-06-28 10:48:23', 13),
	('Hands on Databases', 20, 'Private', '2013-12-05 21:16:45', '2013-10-01 04:19:53', 29),
	('Introduction to Django Admin', 79, 'Private', '2006-09-01 15:24:42', '2006-01-04 13:17:51', 49),
	('Advanced Python', 97, 'Public', '2018-01-04 18:46:35', '2018-01-04 13:44:38', 22),
	('Advanced Django ORM', 44, 'Private', '2018-10-08 11:20:01', '2018-01-23 11:26:27', 6),
	('Hands on Python', 28, 'Public', '2007-06-21 10:32:28', '2007-01-26 16:17:06', 34),
	('Introduction to Django', 84, 'Public', '2012-12-15 03:39:02', '2012-04-03 08:14:15', 1),
	('Hands on Django ORM', 84, 'Private', '2007-05-27 02:56:33', '2007-02-20 08:39:30', 0),
	('Hands on Django', 66, 'Private', '2018-05-09 20:32:18', '2018-02-13 12:12:09', 27),
	('Advanced Python Algorithms', 91, 'Private', '2005-11-23 15:57:30', '2005-04-21 10:54:20', 15),
	('Hands on Django Admin', 17, 'Public', '2010-08-05 08:58:10', '2010-05-03 14:06:35', 13),
	('Hands on Python OOP', 16, 'Public', '2005-01-15 09:03:36', '2005-01-15 09:01:52', 39),
	('Advanced Django', 45, 'Private', '2020-03-19 01:58:04', '2020-03-03 03:19:34', 42),
	('Advanced Python Algorithms', 7, 'Private', '2010-10-15 06:04:30', '2010-05-23 19:45:01', 43),
	('Advanced Django Templates', 55, 'Public', '2010-08-03 22:05:15', '2010-08-02 03:49:49', 1),
	('Introduction to Python Algorithms', 92, 'Private', '2013-09-15 06:00:46', '2013-08-05 13:17:26', 4),
	('Advanced Python Algorithms', 91, 'Private', '2006-09-27 02:47:15', '2006-02-09 01:49:45', 5),
	('Advanced Databases', 73, 'Public', '2010-06-01 04:48:05', '2010-01-25 19:22:20', 38),
	('Introduction to Django', 73, 'Private', '2011-06-07 15:37:08', '2011-03-08 21:13:57', 8),
	('Advanced Django Admin', 38, 'Private', '2006-03-21 10:30:57', '2006-03-18 00:45:03', 44),
	('Introduction to Databases', 48, 'Private', '2006-02-26 18:07:47', '2006-02-04 11:15:31', 5),
	('Introduction to Python OOP', 69, 'Private', '2016-02-14 00:20:35', '2016-02-04 22:45:37', 24),
	('Introduction to Computer', 50, 'Public', '2007-04-02 00:08:11', '2007-01-14 16:07:07', 20),
	('Introduction to Computer', 36, 'Public', '2009-01-28 01:56:44', '2009-01-28 07:28:54', 20),
	('Introduction to Computer', 59, 'Private', '2014-07-05 04:15:00', '2014-03-23 22:42:38', 21),
	('Hands on Databases', 51, 'Public', '2013-12-29 02:41:12', '2013-03-22 01:55:02', 22),
	('Introduction to Django Admin', 104, 'Private', '2014-09-09 21:43:26', '2014-07-30 01:27:18', 15),
	('Introduction to Django', NULL, 'Public', '2008-12-21 01:49:43', '2008-12-20 12:08:09', 10),
	('Hands on Django', 99, 'Public', '2017-08-03 23:27:27', '2017-05-09 08:48:45', 36),
	('Introduction to Django', 84, 'Public', '2006-02-07 01:14:57', '2006-02-05 10:54:39', 25),
	('Advanced Django Templates', 50, 'Public', '2012-11-08 04:56:02', '2012-09-05 10:17:34', 45),
	('Hands on Django ORM', 25, 'Private', '2021-03-01 16:43:11', '2021-03-01 17:55:20', 29),
	('Hands on Django Admin', 52, 'Public', '2018-04-03 19:22:16', '2018-01-06 15:20:37', 8),
	('Hands on Python Algorithms', 14, 'Public', '2019-07-02 07:05:02', '2019-06-11 13:10:55', 35),
	('Hands on Python OOP', 74, 'Public', '2020-07-23 17:54:43', '2020-06-27 05:26:50', 13),
	('Hands on Django Templates', 43, 'Private', '2018-08-08 03:46:18', '2018-03-18 05:38:18', 14),
	('Hands on Django', 46, 'Public', '2019-10-08 19:27:01', '2019-08-21 20:15:40', 10),
	('Introduction to Python', 7, 'Public', '2010-10-15 12:16:17', '2010-06-21 15:19:15', 10),
	('Advanced Django Templates', 85, 'Public', '2015-06-20 00:16:34', '2015-04-26 20:28:02', 34),
	('Hands on Python', 74, 'Public', '2020-05-02 02:13:02', '2020-04-26 10:56:00', 47),
	('Advanced Python Algorithms', 3, 'Public', '2018-04-03 06:35:31', '2018-03-01 18:25:27', 43),
	('Introduction to Django Admin', 31, 'Public', '2018-04-17 21:37:44', '2018-03-16 19:07:23', 44),
	('Hands on Django Admin', 65, 'Public', '2012-10-23 13:41:08', '2012-08-02 18:04:01', 35),
	('Introduction to Django', 91, 'Private', '2005-03-03 10:45:25', '2005-02-09 04:04:16', 33),
	('Advanced Django Admin', 73, 'Public', '2021-05-05 16:36:57', '2021-01-17 10:46:12', 45),
	('Introduction to Django', 72, 'Public', '2005-05-01 06:21:59', '2005-02-23 22:10:14', 35),
	('Advanced Django', 83, 'Private', '2014-06-22 11:26:54', '2014-04-10 22:00:17', 42),
	('Hands on Computer', 42, 'Public', '2019-01-15 18:26:25', '2019-01-15 17:44:01', 25),
	('Advanced Django Templates', 83, 'Public', '2014-06-08 06:54:42', '2014-04-11 20:51:11', 1),
	('Advanced Python OOP', 91, 'Public', '2015-11-04 13:57:51', '2015-10-29 23:20:02', 28),
	('Introduction to Django', 50, 'Public', '2010-02-02 07:18:45', '2010-01-18 11:15:32', 39),
	('Introduction to Computer', 38, 'Private', '2007-10-01 15:54:08', '2007-05-27 04:38:26', 39),
	('Hands on Python OOP', 91, 'Public', '2018-03-06 16:55:48', '2018-02-15 02:53:27', 43),
	('Introduction to Databases', 52, 'Private', '2008-10-13 12:13:50', '2008-06-05 05:16:12', 40),
	('Hands on Python', 36, 'Public', '2016-11-07 13:33:30', '2016-02-19 05:48:59', 43),
	('Advanced Django Admin', 36, 'Private', '2006-10-27 14:25:37', '2006-06-30 23:46:42', 42),
	('Introduction to Django Templates', 79, 'Private', '2018-05-26 14:08:15', '2018-01-27 09:30:18', 48),
	('Hands on Python Algorithms', 33, 'Public', '2019-01-13 06:03:54', '2019-01-13 01:48:50', 21),
	('Advanced Django Admin', 87, 'Private', '2010-09-15 12:42:53', '2010-05-03 00:14:59', 11),
	('Advanced Python Algorithms', 50, 'Private', '2012-03-07 08:43:07', '2012-02-06 18:57:58', 38),
	('Hands on Python Algorithms', 42, 'Private', '2013-08-30 00:27:49', '2013-06-30 04:57:03', 33),
	('Introduction to Python', 7, 'Public', '2013-04-09 10:44:29', '2013-02-13 18:41:23', 36),
	('Introduction to Databases', 83, 'Private', '2012-04-14 12:55:07', '2012-01-16 03:02:43', 18),
	('Introduction to Python', 22, 'Private', '2005-03-18 03:33:50', '2005-01-20 10:26:30', 14),
	('Advanced Django', 3, 'Private', '2006-02-19 16:48:58', '2006-01-28 03:01:49', 27),
	('Introduction to Django Templates', 78, 'Private', '2008-09-15 03:52:40', '2008-07-21 12:00:21', 11),
	('Advanced Django ORM', 76, 'Private', '2018-08-10 19:23:34', '2018-04-26 04:08:09', 25),
	('Hands on Django Admin', 48, 'Public', '2013-10-12 02:24:32', '2013-08-20 16:42:36', 33),
	('Hands on Django', 65, 'Private', '2009-09-25 23:49:56', '2009-06-03 20:05:23', 7),
	('Hands on Computer', 56, 'Public', '2016-01-11 13:32:51', '2016-01-11 04:15:30', 2),
	('Introduction to Computer', 73, 'Private', '2019-09-26 14:13:32', '2019-06-09 10:17:03', 12),
	('Advanced Python Algorithms', 29, 'Private', '2021-05-28 06:11:53', '2021-04-04 18:34:24', 22),
	('Introduction to Python', 1, 'Public', '2011-04-14 14:43:42', '2011-03-10 02:17:08', 35),
	('Advanced Django', 12, 'Private', '2016-08-20 21:44:12', '2016-06-12 21:47:44', 34),
	('Hands on Databases', 26, 'Private', '2014-04-10 03:26:54', '2014-03-01 13:11:49', 45),
	('Advanced Django', 60, 'Private', '2020-03-11 16:38:39', '2020-01-24 16:36:34', 4),
	('Advanced Python Algorithms', 103, 'Public', '2006-12-10 01:03:56', '2006-08-03 11:52:33', 15),
	('Advanced Python Algorithms', 95, 'Public', '2014-04-28 05:28:01', '2014-02-24 05:27:09', 27),
	('Introduction to Computer', 18, 'Public', '2011-05-12 20:57:55', '2011-03-27 02:47:56', 10),
	('Introduction to Django Templates', 73, 'Public', '2020-11-01 04:25:05', '2020-01-04 21:56:26', 5),
	('Introduction to Django Templates', 27, 'Public', '2019-07-24 14:49:37', '2019-06-21 06:33:33', 37),
	('Advanced Django ORM', 44, 'Private', '2017-10-29 12:39:34', '2017-04-24 23:29:12', 30),
	('Hands on Django Templates', 75, 'Public', '2013-09-30 15:54:05', '2013-06-24 10:33:18', 38),
	('Advanced Python OOP', 16, 'Public', '2020-11-26 03:14:07', '2020-09-25 00:10:12', 30),
	('Introduction to Django Admin', 59, 'Public', '2017-03-30 04:02:29', '2017-02-23 17:42:57', 14),
	('Hands on Python', 59, 'Public', '2016-01-23 10:39:17', '2016-01-23 14:29:13', 37),
	('Introduction to Computer', 40, 'Public', '2006-03-03 08:17:23', '2006-01-07 16:19:28', 47),
	('Advanced Databases', 20, 'Public', '2010-08-06 19:43:14', '2010-04-10 16:55:04', 40),
	('Advanced Databases', 27, 'Public', '2019-01-10 19:53:36', '2019-01-10 14:13:33', 37),
	('Introduction to Python', 76, 'Private', '2010-10-09 21:08:06', '2010-03-06 06:08:14', 9),
	('Introduction to Django Admin', 53, 'Public', '2020-09-26 15:38:07', '2020-05-02 13:19:35', 11),
	('Advanced Python Algorithms', 23, 'Private', '2008-07-15 05:34:36', '2008-04-13 20:50:37', 19),
	('Introduction to Python', 104, 'Private', '2005-06-23 00:11:47', '2005-03-23 21:30:39', 46),
	('Advanced Django ORM', 41, 'Private', '2019-12-19 11:09:26', '2019-10-25 09:09:32', 41),
	('Introduction to Python', 96, 'Public', '2008-08-10 06:42:22', '2008-04-16 15:27:20', 34),
	('Advanced Python Algorithms', 86, 'Public', '2013-10-18 21:54:10', '2013-03-27 04:16:32', 28),
	('Advanced Computer', 55, 'Private', '2021-05-04 12:59:55', '2021-01-11 22:38:44', 28),
	('Hands on Python Algorithms', 93, 'Public', '2021-02-24 12:19:10', '2021-02-08 21:00:34', 15),
	('Advanced Python Algorithms', 98, 'Private', '2006-02-16 07:22:11', '2006-01-29 23:11:25', 37),
	('Hands on Django ORM', 16, 'Private', '2010-11-22 13:48:43', '2010-09-07 03:34:33', 49),
	('Advanced Python Algorithms', 80, 'Private', '2013-05-02 03:25:42', '2013-04-04 06:14:03', 1),
	('Advanced Python', 74, 'Private', '2021-06-24 06:31:40', '2021-03-04 00:25:26', 19),
	('Advanced Django', 3, 'Private', '2005-08-17 03:24:24', '2005-07-31 12:47:12', 22),
	('Hands on Python Algorithms', 7, 'Private', '2015-06-13 05:24:29', '2015-05-03 15:30:17', 46),
	('Introduction to Django Templates', 19, 'Public', '2014-06-13 01:33:03', '2014-02-17 10:44:22', 46),
	('Hands on Python OOP', 41, 'Public', '2019-08-19 16:27:19', '2019-04-23 20:54:41', 31),
	('Advanced Python Algorithms', 64, 'Public', '2007-07-25 01:57:55', '2007-06-04 10:03:35', 28),
	('Advanced Django', 74, 'Private', '2015-07-22 06:42:24', '2015-02-13 02:33:01', 24),
	('Introduction to Django Admin', 61, 'Public', '2007-01-30 01:06:57', '2007-01-30 07:11:27', 8),
	('Hands on Django Admin', 43, 'Public', '2013-06-18 10:48:23', '2013-06-03 08:37:17', 25),
	('Advanced Computer', 100, 'Public', '2013-04-22 22:17:24', '2013-03-31 21:55:31', 26),
	('Introduction to Django', 87, 'Private', '2006-01-04 05:59:09', '2006-01-04 02:57:13', 45),
	('Hands on Python OOP', 66, 'Public', '2015-01-28 18:58:07', '2015-01-28 15:20:13', 46),
	('Advanced Django', 35, 'Public', '2008-07-27 04:57:51', '2008-03-20 13:28:24', 41),
	('Introduction to Django Admin', 67, 'Public', '2018-09-27 01:42:36', '2018-08-08 18:27:19', 12),
	('Advanced Django Admin', 72, 'Public', '2015-09-11 14:39:27', '2015-07-06 19:29:07', 20),
	('Introduction to Python OOP', 71, 'Public', '2016-08-19 06:30:24', '2016-01-26 03:14:13', 3),
	('Advanced Databases', 22, 'Public', '2020-12-28 13:19:59', '2020-10-08 12:59:41', 21),
	('Hands on Python Algorithms', 8, 'Private', '2012-11-01 21:29:22', '2012-08-01 12:58:13', 10),
	('Advanced Django ORM', 53, 'Public', '2011-10-28 12:39:34', '2011-07-10 05:32:51', 9),
	('Hands on Python Algorithms', 103, 'Public', '2020-02-26 13:54:49', '2020-02-25 20:32:50', 21),
	('Hands on Computer', 36, 'Private', '2016-11-25 01:10:50', '2016-02-14 20:25:07', 43),
	('Advanced Databases', 82, 'Private', '2006-04-18 01:10:37', '2006-01-29 18:00:24', 7);