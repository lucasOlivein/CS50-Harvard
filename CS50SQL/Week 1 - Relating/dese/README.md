# DESE
### 🚀 Summary
...
### 📄 Description (Adapted)
...
### ⚙️ Specification
<details><summary>📌 <strong>Task:</strong> <em>For each of the following questions, you should write a single SQL query that outputs the results specified by each problem.</em></summary>



- Your response must take the form of a single SQL query. 
- You should not assume anything about the `id`s of any particular rows:
    - your queries should be accurate even if the `id`s were different. 
- Finally, each query should return only the data necessary to answer the question.

</details>

<details><summary> 📋 <strong>Questions:</strong></summary>

<br>

<details><summary>✅ <strong>01</strong>: <em>Your colleague is preparing a map of all public schools in Massachusetts.</em></summary>

<br>

📌 In `1.sql`, write a SQL query to find the names and cities of all public schools in Massachusetts.
- Keep in mind that not all schools in the `schools` table are considered traditional public schools. Massachusetts also recognizes [charter schools](https://en.wikipedia.org/wiki/Charter_schools_in_the_United_States), which (according to DESE!) are considered distinct.

---
</details>

<details><summary>✅ <strong>02</strong>: <em>Your team is working on archiving old data.</em></summary>

<br>

📌 In `2.sql`, write a SQL query to find the names of districts that are no longer operational.
- Districts that are no longer operational have “(non-op)” at the end of their name.

---
</details>

<details><summary>✅ <strong>03</strong>: <em>The Massachusetts Legislature would like to learn how much money, on average, districts spent per-pupil last year.</em></summary>

<br>

📌 In `3.sql`, write a SQL query to find the average per-pupil expenditure. Name the column “Average District Per-Pupil Expenditure”.
- Note the `per_pupil_expenditure` column in the `expenditures` table contains the average amount, per pupil, each district spent last year. You’ve been asked to find the average of this set of averages, weighting all districts equally regardless of their size.

---
</details>

<details><summary>✅ <strong>04</strong>: <em>Some cities have more public schools than others.</em></summary>

<br>

📌 In 4.sql, write a SQL query to find the 10 cities with the most public schools. 
- Your query should return the names of the cities and the number of public schools within them, ordered from greatest number of public schools to least. 
- If two cities have the same number of public schools, order them alphabetically.

---
</details>

<details><summary>✅ <strong>05</strong>: <em>DESE would like you to determine in what cities additional public schools might be needed.</em></summary>

<br>

📌 In `5.sql`, write a SQL query to find cities with 3 or fewer public schools. 
- Your query should return the names of the cities and the number of public schools within them, ordered from greatest number of public schools to least. 
- If two cities have the same number of public schools, order them alphabetically.

---
</details>

<details><summary>✅ <strong>06</strong>: <em>DESE wants to assess which schools achieved a 100% graduation rate.</em></summary>

<br>

📌 In `6.sql`, write a SQL query to find the names of schools (public or charter!) that reported a 100% graduation rate.

---
</details>

<details><summary>✅ <strong>07</strong>: <em>DESE is preparing a report on schools in the Cambridge school district.</em></summary>

<br>

📌 In `7.sql`, write a SQL query to find the names of schools (public or charter!) in the Cambridge school district. 
- Keep in mind that Cambridge, the city, contains a few school districts, but DESE is interested in the district whose name is “Cambridge.”

---
</details>

<details><summary>✅ <strong>08</strong>: <em>A parent wants to send their child to a district with many other students.</em></summary>

<br>

📌 In `8.sql`, write a SQL query to display the names of all school districts and the number of pupils enrolled in each.

---
</details>

<details><summary>✅ <strong>09</strong>: <em>Another parent wants to send their child to a district with few other students.</em></summary>

<br>

📌 In `9.sql`, write a SQL query to find the name (or names) of the school district(s) with the single least number of pupils. Report only the name(s).

---
</details>

<details><summary>✅ <strong>10</strong>: <em>In Massachusetts, school district expenditures are in part determined by local taxes on property (e.g., home) values.</em></summary>

<br>

📌 In `10.sql`, write a SQL query to find the 10 public school districts with the highest per-pupil expenditures. Your query should return the names of the districts and the per-pupil expenditure for each.

---
</details>

<details><summary>✅ <strong>11</strong>: <em>Is there a relationship between school expenditures and graduation rates?</em></summary>

<br>

📌 In `11.sql`, write a SQL query to display the names of schools, their per-pupil expenditure, and their graduation rate. 
- Sort the schools from greatest per-pupil expenditure to least. 
- If two schools have the same per-pupil expenditure, sort by school name.
- ⚠︎ You should assume a school spends the same amount per-pupil their district as a whole spends.

---
</details>

<details><summary>✅ <strong>12</strong>: <em>A parent asks you for advice on finding the best public school districts in Massachusetts.</em></summary>

<br>

📌 In `12.sql`, write a SQL query to find public school districts with above-average per-pupil expenditures and an above-average percentage of teachers rated “exemplary”. 
- Your query should return the districts’ names, along with their per-pupil expenditures and percentage of teachers rated exemplary. 
- Sort the results first by the percentage of teachers rated exemplary (high to low), then by the per-pupil expenditure (high to low).

<details><summary>💡 Hint </summary>

You might find it helpful to know that subqueries can be inserted into most any part of a SQL query, including conditions. For instance, the following is valid SQL syntax:
```sql
SELECT "column" FROM "table"
WHERE "column" > (
    SELECT AVG("column")
    FROM "table"
);
```
</details>

---
</details>

<details><summary>✅ <strong>13</strong>: <em>It is up to you!</em></summary>

<br>

📌 In `13.sql`, write a SQL query to answer a question you have about the data! The query should:
- Involve at least one JOIN or subquery

---
</details>
</details>

### 🎯 Solution
<table>
  <tr>
    <td>

| Question | Commit |
|:---------:|--------|
| 01 | [e0d2557](https://github.com/lucasOlivein/CS50-Harvard/commit/e0d25575c5149553a4bb98e5347f833f7ca83288) |
| 02 | [108e63b](https://github.com/lucasOlivein/CS50-Harvard/commit/108e63b187b7964f8d6ef01ff80fc19aad3647b0) |
| 03 | [a0483ae](https://github.com/lucasOlivein/CS50-Harvard/commit/a0483aeccf93fa49a52ebcabba696cdfe874cad8) |
| 04 | [992df1d](https://github.com/lucasOlivein/CS50-Harvard/commit/992df1d0de30e602c3ebd5cab6d01ffe9459b72b) |
| 05 | [7c7af07](https://github.com/lucasOlivein/CS50-Harvard/commit/7c7af07db40c8d146ff20ac1b83a34217dbb78b9) |
| 06 | [4fa3005](https://github.com/lucasOlivein/CS50-Harvard/commit/4fa300523fa637c3c5027a4dbd4dddd4674a5615) |
| 07 | [4b9e596](https://github.com/lucasOlivein/CS50-Harvard/commit/4b9e596ff3d35cea431e4f93d66f2499adf9ce66) |

</td>
<td valign="top">

| Question | Commit |
|:---------:|--------|
| 08 | [17cafe1](https://github.com/lucasOlivein/CS50-Harvard/commit/17cafe1656a5a057d3a7e73f6128ed4603cdcf31) |
| 09 | [821418c](https://github.com/lucasOlivein/CS50-Harvard/commit/821418c0679321785cb0fa8fda1f9014dab806a8) |
| 10 | [033d6c1](https://github.com/lucasOlivein/CS50-Harvard/commit/033d6c13c53b6dd9168d94b5480229b945d27a7f) |
| 11 | [4ebade3](https://github.com/lucasOlivein/CS50-Harvard/commit/4ebade32842a7ed9236eb52e1efddf249d26b47a) |
| 12 | [0b63dd5](https://github.com/lucasOlivein/CS50-Harvard/commit/0b63dd572966570c29ef1e61eb1068f119cd630b) |
| 13 | [82958b2](https://github.com/lucasOlivein/CS50-Harvard/commit/82958b2724d99d4a2b63ff8a65690f4478b8aaa3) |

</td>
  </tr>
</table>

⚠︎ Queries tested on SQLite 3 only



### 📚 Source
Based on the *DESE* problem from Harvard’s CS50 SQL course: https://cs50.harvard.edu/sql/psets/1/dese/
### 📂 Download
The distribution code: https://cdn.cs50.net/sql/2024/x/psets/1/dese.zip
