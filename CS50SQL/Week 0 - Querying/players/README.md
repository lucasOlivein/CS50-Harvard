This README is available in [Portuguese](README.pt-BR.md).

# Players
## Background

Baseball is a widely popular sport, especially in the United States and Canada. In the game, two teams of nine players alternate between batting (hitting the ball) and fielding (catching and throwing hit balls). Points — known as “runs” — are scored when a player from the batting team hits the ball and successfully reaches all bases before being put “out” by the fielding team. Major League Baseball (MLB), the sport’s primary professional league, has served as the official organization since 1876.

## Problem Description

In this problem, the objective is to answer questions about MLB players using data contained in the `players.db` database, specifically the `players` table, which includes information on athletes who played between the years 1871 and 2023.

## Dataset

For this problem, the database `players.db` along with *ten* empty `.sql` files are provided — an additional, eleventh file is included for the optional question.  
The single table `players` within `players.db` contains the following columns:

- `id`: uniquely identifies each row (player) in the table.
- `first_name`: the first name of the player.
- `last_name`: the last name of the player.
- `bats`: the side (R for right or L for left) the player bats on.
- `throws`: the hand (R for right or L for left) the player throws with.
- `weight`: the player’s weight in pounds.
- `height`: the player’s height in inches.
- `debut`: the date (expressed as YYYY-MM-DD) the player began their career in the MLB.
- `final_game`: the date (expressed as YYYY-MM-DD) the player played their last game in the MLB.
- `birth_year`: the year the player was born.
- `birth_month`: the month (as an integer) the player was born.
- `birth_day`: the day the player was born.
- `birth_city`: the city in which the player was born.
- `birth_state`: the state in which the player was born.
- `birth_country`: the country in which the player was born.

## Specification

- Each query should consist of a single `SELECT` statement.
- No assumptions should be made about the `id` values — queries must remain valid regardless of those values.
- Each query should return **only** the data necessary to answer the question.
- Each SQL query must be written in a separate file, named according to the corresponding question number (e.g., `1.sql` for question 1, `2.sql` for question 2, and so on).

## Questions
Below is a description of the 11 questions answered in this problem set.

- [X] **Q1:** Find the hometown (including city, state, and country) of Jackie Robinson.
- [X] **Q2:** Find the side (e.g., right or left) Babe Ruth hit.
- [X] **Q3:** Find the ids of rows for which a value in the column `debut` is missing.
- [X] **Q4:** Find the first and last names of players who were not born in the United States. Sort the results alphabetically by first name, then by last name.
- [X] **Q5:** Return the first and last names of all right-handed batters. Sort the results alphabetically by first name, then by last name.
- [X] **Q6:** Return the first name, last name, and debut date of players born in Pittsburgh, Pennsylvania (PA). Sort the results first by debut date — from most recent to oldest — then alphabetically by first name, followed by last name.
- [X] **Q7:** Count the number of players who bat (or batted) right-handed and throw (or threw) left-handed, or vice versa.
- [X] **Q8:** Find the average height and weight, rounded to two decimal places, of baseball players who debuted on or after January 1st, 2000. Return the columns with the names “Average Height” and “Average Weight”, respectively.
- [X] **Q9:** Find the players who played their final game in the MLB in 2022. Sort the results alphabetically by first name, then by last name.
- [X] **Q10:** Answer a question of your choice. This query should:
    - Make use of `AS` to rename a column.
    - Include at least one condition using `WHERE`.
    - Sort by at least one column using `ORDER BY`.

**Optional:**
- [X] **Q11:** List the first and last names of all players of above average height, sorted tallest to shortest, then by first and last name.

## Source

This README was based on the documentation of the *Players* problem from Harvard University's course **CS50’s Introduction to Databases with SQL**, available at: [https://cs50.harvard.edu/sql/2024/psets/0/players/](https://cs50.harvard.edu/sql/2024/psets/0/players/)
