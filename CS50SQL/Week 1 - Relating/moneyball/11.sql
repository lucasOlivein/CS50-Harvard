-- Q11. Find the 10 least expensive players per hit in 2001.
--
-- - Your query should return a table with three columns, 
--   - one for the players’ first names, 
--   - one of their last names, and
--   - one called “dollars per hit”.
-- - You can calculate the “dollars per hit” column by dividing a player’s 
--   2001 salary by the number of hits they made in 2001. Recall you can use 
--   AS to rename a column.
--
-- - Dividing a salary by 0 hits will result in a NULL value. 
--   Avoid the issue by filtering out players with 0 hits.
--
-- - Sort the table by the “dollars per hit” column, least to most expensive. 
--   If two players have the same “dollars per hit”, order by first name, 
--   followed by last name, in alphabetical order.
--
-- - As in 10.sql, ensure that the salary’s year and the performance’s 
--   year match.
--
-- - You may assume, for simplicity, that a player will 
--   only have one salary and one performance in 2001.
--
-- The "players" table contains the following columns:
--  "id", "first_name", "last_name", "bats", "throws", "weight",
--  "height", "debut", "final_game", "birth_year", "birth_month", 
--  "birth_day", "birth_city", "birth_state", and "birth_country"
--
-- The "performances" table contains the following columns:
--  "id", "player_id", "team_id", "year", "G", "AB", "H",
--  "2B", "3B", "HR", "RBI", "SB"
--
-- The "salaries" table contains the following columns:
--  "id", "player_id", "team_id", "year" and "salary"
--
-- Answer:
SELECT "first_name", "last_name", ("salaries"."salary" / "performances"."H") AS "dollar per hit"
FROM "players"
JOIN "performances" ON "performances"."player_id" = "players"."id"
JOIN "salaries" ON "salaries"."player_id" = "players"."id"
WHERE "performances"."year" = 2001 
    AND "salaries"."year" = 2001
    AND "performances"."H" != 0
ORDER BY "dollar per hit"
LIMIT 10
;

-- Result: OK
-- 3 columns and 10 rows.