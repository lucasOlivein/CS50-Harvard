-- Q1. Find the average player salary by year.
--
-- - Sort by year in descending order.
-- - Round the salary to two decimal places and call the column “average salary”.
-- - Your query should return a table with two columns, one for year and one for average salary.
--
-- The "salaries" table contains the following columns:
--  "id", "player_id", "team_id", "year" and "salary"
-- 
-- Answer:
SELECT "year", ROUND(AVG("salary"), 2) AS "average salary"
FROM "salaries"
GROUP BY "year"
ORDER BY "year" DESC;

-- Result: OK
-- 2 columns and 17 rows.