# Moneyball

### 🚀 Summary
...
### 📄 Description (Adapted)
...
### ⚙️ Specification
#### 📋 Questions

<details><summary> ✅ <strong>01</strong>: <em>You should start by getting a sense for how average player salaries have changed over time.</em></summary>

<br> 

📌 In `1.sql`, write a SQL query to find the average player salary by year.
- Sort by year in descending order.
- Round the salary to two decimal places and call the column “average salary”.
- Your query should return a table with two columns, one for year and one for average salary.
---
</details>
<details><summary> ✅ <strong>02</strong>: <em>Your general manager (i.e., the person who makes decisions about player contracts) asks you whether the team should trade a current player for Cal Ripken Jr., a star player who’s likely nearing his retirement.</em></summary>

<br>

📌 In `2.sql`, write a SQL query to find Cal Ripken Jr.’s salary history.
- Sort by year in descending order.
- Your query should return a table with two columns, one for year and one for salary.
---
</details>
<details><summary> ✅ <strong>03</strong>: <em>Your team is going to need a great home run hitter. Ken Griffey Jr., a long-time Silver Slugger and Gold Glove award winner, might be a good prospect.</em></summary>

<br>

📌 In `3.sql`, write a SQL query to find Ken Griffey Jr.’s home run history.

- Sort by year in descending order.
- Note that there may be two players with the name “Ken Griffey.” This Ken Griffey was born in 1969.
- Your query should return a table with two columns, one for year and one for home runs.
---
</details>
<details><summary> ✅ <strong>04</strong>: <em>You need to make a recommendation about which players the team should consider hiring. With the team’s dwindling budget, the general manager wants to know which players were paid the lowest salaries in 2001.</em></summary>

<br>

📌 In `4.sql`, write a SQL query to find the 50 players paid the least in 2001.

- Sort players by salary, lowest to highest.
- If two players have the same salary, sort alphabetically by first name and then by last name.
- If two players have the same first and last name, sort by player ID.
- Your query should return three columns, one for players’ first names, one for their last names, and one for their salaries.
---
</details>
<details><summary> ✅ <strong>05</strong>: <em>It’s a bit of a slow day in the office.</em></summary>

<br>

_Though Satchel no longer plays,_    

📌 in `5.sql`, write a SQL query to find all teams that [Satchel Paige](https://en.wikipedia.org/wiki/Satchel_Paige) played for.

- Your query should return a table with a single column, one for the name of the teams.
---
</details>
<details><summary> ✅ <strong>06</strong>: <em>Which teams might be the biggest competition for the A’s this year?</em></summary>

<br>

📌 In `6.sql`, write a SQL query to return the top 5 teams, sorted by the total number of hits by players in 2001.

- Call the column representing total hits by players in 2001 “total hits”.
- Sort by total hits, highest to lowest.
- Your query should return two columns, one for the teams’ names and one for their total hits in 2001.

</details>
<details><summary> ✅ <strong>07</strong>: <em>You need to make a recommendation about which player (or players) to avoid recruiting.</em></summary>

<br>

📌 In `7.sql`, write a SQL query to find the name of the player who’s been paid the highest salary, of all time, in Major League Baseball.

- Your query should return a table with two columns, one for the player’s first name and one for their last name.
---
</details>
<details><summary> ✅ <strong>08</strong>: <em>How much would the A’s need to pay to get the best home run hitter this past season?</em></summary>

<br>

📌 In `8.sql`, write a SQL query to find the 2001 salary of the player who hit the most home runs in 2001.

- Your query should return a table with one column, the salary of the player.
---
</details>
<details><summary> ✅ <strong>09</strong>: <em>What salaries are other teams paying?</em></summary>

<br>

📌 In `9.sql`, write a SQL query to find the 5 lowest paying teams (by average salary) in 2001.

- Round the average salary column to two decimal places and call it “average salary”.
- Sort the teams by average salary, least to greatest.
- Your query should return a table with two columns, one for the teams’ names and one for their average salary.
---
</details>
<details><summary> ✅ <strong>10</strong>: <em>The general manager has asked you for a report which details each player’s name, their salary for each year they’ve been playing, and their number of home runs for each year they’ve been playing.</em></summary>

<br>
    
To be precise, the table should include:

- All player’s first names
- All player’s last names
- All player’s salaries
- All player’s home runs
- The year in which the player was paid that salary and hit those home runs

📌 In `10.sql`, write a query to return just such a table.

- Your query should return a table with five columns, per the above.
- Order the results, first and foremost, by player’s IDs (least to greatest).
- Order rows about the same player by year, in descending order.
- Consider a corner case: suppose a player has multiple salaries or performances for a given year. Order them first by number of home runs, in descending order, followed by salary, in descending order.
- Be careful to ensure that, for a single row, the salary’s year and the performance’s year match.

<details><summary><strong>Example table</strong></summary>

To help you visualize what the general manager would like, they gave you an example table:
```
+------------+-----------+--------+------+----+
| first_name | last_name | salary | year | HR |
+------------+-----------+--------+------+----+
| Don        | Aase      | 400000 | 1989 | 0  |
| Don        | Aase      | 675000 | 1988 | 0  |
| Don        | Aase      | 625000 | 1987 | 0  |
| Don        | Aase      | 600000 | 1986 | 0  |
| Jeff       | Abbott    | 300000 | 2001 | 0  |
| Jeff       | Abbott    | 255000 | 2000 | 3  |
| Jeff       | Abbott    | 255000 | 1999 | 2  |
+------------+-----------+--------+------+----+
```
If all goes well, you might also see two rows like this in your final table:
```
+-------------+---------------+----------+----+------+
| first_name  | last_name     | salary   | HR | year |
+-------------+---------------+----------+----+------+
| Todd        | Zeile         | 3700000  | 9  | 1995 |
| Todd        | Zeile         | 3700000  | 5  | 1995 |
+-------------+---------------+----------+----+------+
```
As an aside, based on the schema of the database, why do you think Todd Zeile appears to have two different salaries (and two different HR counts) for the same year?
</details>

---
</details>
<details><summary> ✅ <strong>11</strong>: <em>You need a player that can get hits. Who might be the most underrated?</em></summary>

<br>

📌 In `11.sql`, write a SQL query to find the 10 least expensive players per hit in 2001.

- Your query should return a table with three columns, one for the players’ first names, one of their last names, and one called “dollars per hit”.
- You can calculate the “dollars per hit” column by dividing a player’s 2001 salary by the number of hits they made in 2001. Recall you can use AS to rename a column.
- Dividing a salary by 0 hits will result in a NULL value. Avoid the issue by filtering out players with 0 hits.
- Sort the table by the “dollars per hit” column, least to most expensive. If two players have the same “dollars per hit”, order by first name, followed by last name, in alphabetical order.
- As in 10.sql, ensure that the salary’s year and the performance’s year match.
- You may assume, for simplicity, that a player will only have one salary and one performance in 2001.

</details>
<details><summary> ✅ <strong>12</strong>: <em>Hits are great, but so are RBIs!</em></summary>

<br>

📌 In `12.sql`, write a SQL query to find the players among the 10 least expensive players per hit and among the 10 least expensive players per RBI in 2001.

- Your query should return a table with two columns, one for the players’ first names and one of their last names.
- You can calculate a player’s salary per RBI by dividing their 2001 salary by their number of RBIs in 2001.
- You may assume, for simplicity, that a player will only have one salary and one performance in 2001.
- Order your results by player ID, least to greatest (or alphabetically by last name, as both are the same in this case!).
- Keep in mind the lessons you’ve learned in 10.sql and 11.sql!

</details>


### 🎯 Solution


<table>
  <tr>
    <td>

| Question | Commit |
|:---------:|--------|
| 01 | [5544085](https://github.com/lucasOlivein/CS50-Harvard/commit/5544085a7d62591a133dad2516e478d62d8dcd16) |
| 02 | [12f5043](https://github.com/lucasOlivein/CS50-Harvard/commit/12f50436506b330e1a0749c7fcb58924865462ac) |
| 03 | [a41b972](https://github.com/lucasOlivein/CS50-Harvard/commit/a41b9720cf9f883baf19f8e8c1dfdba6272a7fee) |
| 04 | [db9b82e](https://github.com/lucasOlivein/CS50-Harvard/commit/db9b82e869bbf5c6b47b12bc41da0f8cce8c1451) |
| 05 | [08153cb](https://github.com/lucasOlivein/CS50-Harvard/commit/08153cb0ec4f4772f33dd445ea97b3eb5fb456cb) |
| 06 | [90546a0](https://github.com/lucasOlivein/CS50-Harvard/commit/90546a022e62184fb78ab9b5d687dc061fbd03f0) |


</td>
<td valign="top">

| Question | Commit |
|:---------:|--------|
| 07 | [4455f72](https://github.com/lucasOlivein/CS50-Harvard/commit/4455f72885e717ce6c0b429969ebbb889ac7dfba) |
| 08 | [8f6b2d8](https://github.com/lucasOlivein/CS50-Harvard/commit/8f6b2d8d80db725fe7deeb9dc564689251882aa3) |
| 09 | [e416f44](https://github.com/lucasOlivein/CS50-Harvard/commit/e416f4491ce557123dd0ad619bd91fda54f244ec) |
| 10 | [67163b2](https://github.com/lucasOlivein/CS50-Harvard/commit/67163b261bd095251d1b20468e1e2c9983abab0d) |
| 11 | [1c8a8fd](https://github.com/lucasOlivein/CS50-Harvard/commit/1c8a8fd01c4eb639cddf86f44e73bb44d8231f5e) |
| 12 | [0827fa6](https://github.com/lucasOlivein/CS50-Harvard/commit/0827fa618e78a4803c5aaadadb07e42143416120) |


</td>
  </tr>
</table>

⚠︎ Queries tested on SQLite 3 only

### 📚 Source
Based on the *Moneyball* problem from Harvard’s CS50 SQL course: https://cs50.harvard.edu/sql/psets/1/moneyball/
### 📂 Download
The distribution code: https://cdn.cs50.net/sql/2024/x/psets/1/moneyball.zip