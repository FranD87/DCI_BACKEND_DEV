# Advanced SQL - Aggregate functions

## Description

In this exercise, we will practice a little more on complex uses of grouping, aggregating, joining and filtering.

##

## Data

This exercise uses the data from the previous exercise. If you don't have that data any more, you can create a new database and execute the file [src/data/initial.sql](src/data/initial.sql).

##

## Tasks

###

### Task 1

Produce a list with the top 10 most popular teachers.

> We define *popularity** as the average registrations per webinar. The higher the average registrations, the higher the popularity.

The output should include the name of the teacher and the average registrations, and it should be sorted by average registrations, with the highest first.

If two teachers have the same average webinar registrations, then it should be sorted by total amount of registrations. If they have the same amount, it should be sorted by teacher's name.

- Your output should look like this:

| Teacher          | Average registrations |
|------------------|-----------------------|
| Ella Fiedler     | 47                    |
| Itziar Lewis     | 39                    |
| Emma Schumacher  | 35                    |
| Camila Hill      | 34.5                  |
| Ahmed Anniston   | 33                    |
| Gerald Müller    | 32                    |
| Arturo Nguyen    | 31.3333333333333      |
| Julia Griesebner | 31.3333333333333      |
| Aarya Masferrer  | 31                    |
| Yussef Young     | 31                    |


###

### Task 2

Now produce a list of all teachers whose webinar's popularity is higher than the overall average of registrations per webinar.

- Your result should be sorted by average registrations and should look like this:

| Teacher              | Average registrations |
|----------------------|-----------------------|
| Ella Fiedler         | 47                    |
| Itziar Lewis         | 39                    |
| Emma Schumacher      | 35                    |
| Camila Hill          | 34.5                  |
| Ahmed Anniston       | 33                    |
| Gerald Müller        | 32                    |
| Arturo Nguyen        | 31.3333333333333      |
| Julia Griesebner     | 31.3333333333333      |
| Yussef Young         | 31                    |
| Aarya Masferrer      | 31                    |
| Chloe Anniston       | 31                    |
| Noah O'Connor        | 30.6666666666667      |
| Gianna O'Connor      | 30.5                  |
| Arturo JAckson       | 30.3333333333333      |
| Arnold Griesebner    | 29.5                  |
| Nikolas Young        | 29                    |
| Marc Nguyen          | 29                    |
| Johann White         | 29                    |
| Nikolas White        | 29                    |
| Abdul Smith          | 28.6666666666667      |
| Abdul Wright         | 28.5                  |
| Zain Adams           | 28.4                  |
| Abigail Young        | 28.3333333333333      |
| David Davis          | 28.25                 |
| Loretta Wilson       | 28                    |
| Yussef Lee           | 28                    |
| David Anniston       | 27.8                  |
| Abdul Allen          | 27.6666666666667      |
| Yussef Clark         | 27.5                  |
| Grace McDonald       | 27                    |
| William Smith        | 27                    |
| Benjamin Black       | 27                    |
| Johann Muller        | 26.75                 |
| Marc Adams           | 26.6666666666667      |
| Gerald Muller        | 26.6666666666667      |
| Olivia Ali           | 26.5                  |
| Itziar Hunter        | 26.5                  |
| Penelope O'Connor    | 26.5                  |
| Lucas Swcharzenegger | 26.5                  |
| Nikolas Davis        | 26                    |
| Loretta Young        | 26                    |
| Yussef Anniston      | 26                    |
| Amelia Lewis         | 26                    |
| Ella Garcia          | 25.6666666666667      |
| Gerald Perez         | 25.6666666666667      |


###

### Task 3

Now produce a list of cities with popular teachers (avg registrations above the general avg).

This list should show the name of the city, the amount of popular teachers and the average registrations of all those teachers together (should not take into account the non-popular teachers for this metric).

- Your result should be sorted by the city's average popularity level and it should look like this:

| City        | Popular teachers | Average registrations |
|-------------|------------------|-----------------------|
| Sheffield   | 1                | 39                    |
| Prague      | 2                | 36.75                 |
| Antwerp     | 1                | 33                    |
| Dresden      | 2                | 31.5                  |
| Madrid      | 1                | 31.3333333333333      |
| Frankfurt   | 1                | 31.3333333333333      |
| Moscow      | 1                | 31                    |
| Berlin      | 1                | 30.6666666666667      |
| Ottawa      | 2                | 30.5833333333333      |
| Adelaide    | 3                | 29.8888888888889      |
| Brussels    | 2                | 29.75                 |
| Sarajevo    | 1                | 29.5                  |
| Graz        | 4                | 29.0833333333333      |
| Munich      | 1                | 29                    |
| Malmo       | 1                | 29                    |
| Toulouse    | 2                | 28.5                  |
| Marseille   | 1                | 28.4                  |
| Sydney      | 1                | 28.3333333333333      |
| Barcelona   | 1                | 27.5                  |
| San Marino  | 2                | 27.15                 |
| Auckalnd    | 1                | 27                    |
| Bilbao      | 1                | 27                    |
| Vancouver   | 1                | 27                    |
| Salzburg    | 2                | 26.9583333333333      |
| Xiamen      | 2                | 26.8333333333333      |
| Mildura     | 2                | 26.8333333333333      |
| Chicago     | 1                | 26.75                 |
| Kiev        | 1                | 26.6666666666667      |
| Leipzig     | 1                | 26.5                  |
| Donetsk     | 1                | 26                    |
| Los Angeles | 1                | 26                    |
