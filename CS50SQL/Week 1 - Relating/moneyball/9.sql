-- Q9.  Find the 5 lowest paying teams (by average salary) in 2001.
-- 
-- - Round the average salary column to two decimal places and call 
--   it “average salary”.
-- - Sort the teams by average salary, least to greatest.
-- - Your query should return a table with two columns, 
--   one for the teams’ names and one for their average salary.
-- 
-- The "salaries" table contains the following columns:
--  "id", "player_id", "team_id", "year" and "salary"
--
-- The "teams" table contains the following columns:
--  "id", "year", "name", "park"
--
-- Answer:
SELECT "teams"."name", ROUND(AVG("salary"), 2) AS "average salary"
FROM "salaries"
JOIN "teams" ON "salaries"."team_id" = "teams"."id"
WHERE "salaries"."year" = 2001
GROUP BY "team_id"
ORDER BY "average salary"
LIMIT 5;

-- Result: OK
-- 2 columns and 5 rows.