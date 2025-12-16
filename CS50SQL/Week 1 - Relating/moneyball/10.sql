-- Q10. Find each player’s name, their salary for each
-- year they’ve been playing, and their number of home 
-- runs for each year they’ve been playing.
-- 
-- - The table should include:
--      - All player’s first names
--      - All player’s last names
--      - All player’s salaries
--      - All player’s home runs
--      - The year in which the player was paid that salary
--      - and hit those home runs
--
-- - Your query should return a table with five columns, per the above.
-- - Order the results, first and foremost, by player’s IDs (least to greatest).
-- - Order rows about the same player by year, in descending order.
-- - Consider a corner case: suppose a player has multiple salaries 
--   or performances for a given year. Order them first by number of 
--   home runs, in descending order, followed by salary, in descending order.
-- - Be careful to ensure that, for a single row, the salary’s year 
--   and the performance’s year match.
-- 
-- The "salaries" table contains the following columns:
--  "id", "player_id", "team_id", "year" and "salary"
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
-- The "teams" table contains the following columns:
--  "id", "year", "name", "park"
--
-- Answer:
-- SELECT COUNT(*) FROM(
SELECT "first_name", "last_name", "salary", "HR", "performances"."year"
FROM "players" 
JOIN "salaries" ON "players"."id" = "salaries"."player_id" -- ok
JOIN "performances" ON "players"."id" = "performances"."player_id" -- ok
JOIN "teams" ON "performances"."team_id" = "teams"."id" -- or
-- JOIN "teams" ON "salaries"."team_id" = "teams"."id"
WHERE "performances"."year" = "salaries"."year"
ORDER BY "players"."id", "performances"."year" DESC, "HR" DESC, "salary" DESC
-- )
;

-- Result: Ok
-- 5 columns and 14,915 rows.