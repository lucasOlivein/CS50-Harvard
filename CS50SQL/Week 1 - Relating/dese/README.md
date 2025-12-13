# DESE
### 🚀 Summary
...
### 📄 Description (Adapted)
...
### ⚙️ Specification
📌 For each of the following questions, you should write a single SQL query that outputs the results specified by each problem. 
- Your response must take the form of a single SQL query. 
- You should not assume anything about the `id`s of any particular rows:
    - your queries should be accurate even if the `id`s were different. 
- Finally, each query should return only the data necessary to answer the question.

#### 📋 Questions
<details><summary>⬜ <code>1.sql</code></summary>

_Your colleague is preparing a map of all public schools in Massachusetts._ 
📌 In `1.sql`, write a SQL query to find the names and cities of all public schools in Massachusetts.
- Keep in mind that not all schools in the `schools` table are considered traditional public schools. Massachusetts also recognizes [charter schools](https://en.wikipedia.org/wiki/Charter_schools_in_the_United_States), which (according to DESE!) are considered distinct.

---
</details>

<details><summary>⬜ <code>2.sql</code></summary>

_Your team is working on archiving old data._
📌 In `2.sql`, write a SQL query to find the names of districts that are no longer operational.
- Districts that are no longer operational have “(non-op)” at the end of their name.

---
</details>

<details><summary>⬜ <code>3.sql</code></summary>

_The Massachusetts Legislature would like to learn how much money, on average, districts spent per-pupil last year._ 
📌 In `3.sql`, write a SQL query to find the average per-pupil expenditure. Name the column “Average District Per-Pupil Expenditure”.
- Note the `per_pupil_expenditure` column in the `expenditures` table contains the average amount, per pupil, each district spent last year. You’ve been asked to find the average of this set of averages, weighting all districts equally regardless of their size.

---
</details>

<details><summary>⬜ <code>4.sql</code></summary>

_Some cities have more public schools than others._ 
📌 In 4.sql, write a SQL query to find the 10 cities with the most public schools. 
- Your query should return the names of the cities and the number of public schools within them, ordered from greatest number of public schools to least. 
- If two cities have the same number of public schools, order them alphabetically.

---
</details>

<details><summary>⬜ <code>5.sql</code></summary>

_DESE would like you to determine in what cities additional public schools might be needed._ 
📌 In `5.sql`, write a SQL query to find cities with 3 or fewer public schools. 
- Your query should return the names of the cities and the number of public schools within them, ordered from greatest number of public schools to least. 
- If two cities have the same number of public schools, order them alphabetically.

---
</details>

<details><summary>⬜ <code>6.sql</code></summary>

_DESE wants to assess which schools achieved a 100% graduation rate._ 
📌 In `6.sql`, write a SQL query to find the names of schools (public or charter!) that reported a 100% graduation rate.

---
</details>

<details><summary>⬜ <code>7.sql</code></summary>

_DESE is preparing a report on schools in the Cambridge school district._ 
📌 In `7.sql`, write a SQL query to find the names of schools (public or charter!) in the Cambridge school district. 
- Keep in mind that Cambridge, the city, contains a few school districts, but DESE is interested in the district whose name is “Cambridge.”

---
</details>

<details><summary>⬜ <code>8.sql</code></summary>

_A parent wants to send their child to a district with many other students._ 
📌 In `8.sql`, write a SQL query to display the names of all school districts and the number of pupils enrolled in each.

---
</details>

<details><summary>⬜ <code>9.sql</code></summary>

_Another parent wants to send their child to a district with few other students._
📌 In `9.sql`, write a SQL query to find the name (or names) of the school district(s) with the single least number of pupils. Report only the name(s).

---
</details>

<details><summary>⬜ <code>10.sql</code></summary>

_In Massachusetts, school district expenditures are in part determined by local taxes on property (e.g., home) values._ 
📌 In `10.sql`, write a SQL query to find the 10 public school districts with the highest per-pupil expenditures. Your query should return the names of the districts and the per-pupil expenditure for each.

---
</details>

<details><summary>⬜ <code>11.sql</code></summary>

_Is there a relationship between school expenditures and graduation rates?_
📌 In `11.sql`, write a SQL query to display the names of schools, their per-pupil expenditure, and their graduation rate. 
- Sort the schools from greatest per-pupil expenditure to least. 
- If two schools have the same per-pupil expenditure, sort by school name.
- ⚠︎ You should assume a school spends the same amount per-pupil their district as a whole spends.

---
</details>

<details><summary>⬜ <code>12.sql</code></summary>

_A parent asks you for advice on finding the best public school districts in Massachusetts._
In `12.sql`, write a SQL query to find public school districts with above-average per-pupil expenditures and an above-average percentage of teachers rated “exemplary”. 
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

<details><summary>⬜ <code>13.sql</code></summary>

In `13.sql`, write a SQL query to answer a question you have about the data! The query should:
- Involve at least one JOIN or subquery

---
</details>







### 🎯 Solution
### 📚 Source
Based on the *DESE* problem from Harvard’s CS50 SQL course: https://cs50.harvard.edu/sql/psets/1/dese/
### 📂 Download
The distribution code: https://cdn.cs50.net/sql/2024/x/psets/1/dese.zip