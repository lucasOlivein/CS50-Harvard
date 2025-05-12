# Cyberchase
## Problem Description

In this problem, a database named `cyberchase.db` is provided, containing information about episodes from the PBS show *Cyberchase*. The database includes a single table called `episodes`, and the task is to write SQL queries that answer a series of questions based on the provided data.


## Specification

- Each query should consist of a single `SELECT` statement.
- No assumptions should be made about the `id` values of specific episodes — queries must remain valid regardless of those values.
- Each query should return **only** the data necessary to answer the question — if the question asks for episode titles, other information such as air dates should not be include in the result.



## Dataset
For this problem, the database `cyberchase.db` along side with *thirteen* .sql empty files are provide.
The single table `episodes` within `cyberchase.db` comes with the follow columns:
- `id`: uniquely idenfy a row in the table.
- `season`: the season number wich the episode aired.
- `episode_in_season`: the episode's number in its season.
- `title`: the episode's title.
- `topic`: identifies the ideias the episode teach.
- `air_date`: the date (YYYY-MM-DD) on which the episode 'aired'.
- `product_code`: the unique ID used by PBS internally to refer to each episode.


## Questions

Below is a list of the 13 questions to be answered using SQL queries.  
Each SQL query must be written in a separate file, named according to the corresponding question number (e.g., 1.sql for question 1, 2.sql for question 2, and so on).

- [X] **Q1:** List the titles of all episodes in Season 1.
- [X] **Q2:** List the season number and title of the first episode of every season.
- [X] **Q3:** Find the production code for the episode titled “Hackerized!”.
- [X] **Q4:** Find the titles of episodes that do not have a listed topic.
- [X] **Q5:** Find the title of the holiday episode that aired on December 31st, 2004.
- [X] **Q6:** List the titles of episodes from Season 6 (2008) that were released early, in 2007.
- [X] **Q7:** List the titles and topics of all episodes that teach fractions.
- [X] **Q8:** Count the number of episodes released between 2018 and 2023 (inclusive).
- [X] **Q9:** Count the number of episodes released in Cyberchase’s first six years (2002–2007, inclusive).
- [X] **Q10:** List the IDs, titles, and production codes of all episodes, ordered by production code (earliest to latest).
- [X] **Q11:** List the titles of episodes from Season 5, in reverse alphabetical order.
- [X] **Q12:** Count the number of unique episode titles.
- [X] **Q13:** Write a query of your own choice that includes at least one condition using `WHERE` with `AND` or `OR`.


## Hints Provided

- The `BETWEEN` operator can be used with dates, e.g.:
  
  ```sql
  WHERE air_date BETWEEN '2000-01-01' AND '2000-12-31'
  ```

## Source
This README was based on the documentation of the *Cyberchase* problem from Harvard University's course **CS50’s Introduction to Databases with SQL**, available at:  
[https://cs50.harvard.edu/sql/2023/problems/0/cyberchase](https://cs50.harvard.edu/sql/2023/problems/0/cyberchase)
