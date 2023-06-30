# Advanced SQL - Aggregate functions

## Description

In this exercise, we will practice on more complex uses of all the knowledge acquired in this module.

##

## Data

This exercise uses the data from the previous exercise. If you don't have that data any more, you can create a new database and execute the file [src/data/initial.sql](src/data/initial.sql).

##

## Tasks

###

### Task 1

With the data from the previous exercise, produce a list of teachers with their name, how many webinars they offered, and the total students registered to those webinars.

> HINT: If the teacher didn't offer any webinar it should show 0 webinars.

Sort the output by teacher's name.

- Your result should look like this:

| Teacher          | Webinars | Registrations |
|------------------|----------|---------------|
| Aaliyah Lewis    | 1        | 19            |
| Aaliyah Miller   | 1        | 20            |
| Aarya Masferrer  | 2        | 62            |
| Abdul Allen      | 3        | 83            |
| Abdul Griesebner | 2        | 40            |
| Abdul Smith      | 3        | 86            |
| Abdul Wright     | 2        | 57            |
| Abigail Hunter   | 3        | 59            |
| Abigail Young    | 3        | 85            |
| Ahmed Allen      | 0        | 0             |
| Ahmed Anniston   | 2        | 66            |
| Ahmed Lewis      | 2        | 44            |
| Amelia Lewis     | 1        | 26            |
| ...              | ...      | ...           |


###

### Task 2

Find out which teachers did not offer any webinar.

> Write two different SQL statements to accomplish this. One should use a `JOIN` clause and the other one should not.

- Your result should be the same in both statements, it should be sorted by teacher's name and should look like this:

| id  | name                 | city      |
|-----|----------------------|-----------|
| 6   | Ahmed Allen          | Auckalnd  |
| 81  | Anna Wright          | Donetsk   |
| 89  | Araceli Young        | Graz      |
| 57  | Benjamin Hunter      | Seattle   |
| 101 | Benjamin Smith       | Sheffield |
| 37  | Bernhard Johnson     | Dortmund  |
| 10  | Bernhard Moore       | Tubingen  |
| 21  | Chloe Swcharzenegger | Auckalnd  |
| 102 | Ella O'Connor        | Malmo     |
| 62  | Emma Ahmas           | Graz      |
| 58  | Evelyn Hunter        | Dublin    |
| 90  | Mia Müller           | Antwerp   |
| 68  | Yussef Miller        | Munich    |
| 24  | Yussef Wright        | Venice    |
| 105 | Zain Moore           | Graz      |

###

### Task 3

Find out how many students have mentors who did not offer any webinar.

> Again, write two different SQL statements: one with a `JOIN` clause and one without.

- Your result should look like this:

| count |
|-------|
| 420   |

### Task 4

Find out how many webinars did each of the students from the previous task (those whose mentors didn't offer any webinar) attend.

> Your result should include the name of the student and the amount of webinars attended.
>
> It should only include the students whose mentors have not offered any webinar ever.

- Your result should look like this:

| Student          | Webinars attended |
|------------------|------------------ |
| Aaliyah Ali      | 2                 |
| Aaliyah Black    | 0                 |
| Aaliyah Garcia   | 1                 |
| Aaliyah Jones    | 0                 |
| Aaliyah McDonald | 2                 |
| Aaliyah Miller   | 2                 |
| Aaliyah Moore    | 0                 |
| Aaliyah Moore    | 3                 |
| Aaliyah Perez    | 6                 |
| Aaliyah Wilson   | 0                 |
| Aarya Hill       | 4                 |
| Aarya Hunter     | 3                 |
| Aarya Johnson    | 5                 |
| Aarya Lewis      | 6                 |
| Aarya Moore      | 4                 |
| ...              | ...               |
