-- Q4. Find the 50 players paid the least in 2001.
--
-- - Sort players by salary, lowest to highest.
-- - If two players have the same salary, 
--   sort alphabetically by first name and then by last name.
-- - If two players have the same first and last name, 
--   sort by player ID.
-- - Your query should return three columns, one for players’ first names
--   one for their last names, and one for their salaries.
--
-- The "salaries" table contains the following columns:
--  "id", "player_id", "team_id", "year" and "salary"
--
-- The "players" table contains the following columns:
--  "id", "first_name", "last_name", "bats", "throws", "weight",
--  "height", "debut", "final_game", "birth_year", "birth_month", 
--  "birth_day", "birth_city", "birth_state", and "birth_country"
--
-- Answer:
SELECT "first_name", "last_name", "salary"
FROM "players" 
JOIN "salaries" ON "players"."id" = "salaries"."player_id"
WHERE "year" = 2001
ORDER BY "salary" ASC, "first_name", "last_name", "players"."id"
LIMIT 50;

-- Result: OK
-- 3 columns and 50 rows.
