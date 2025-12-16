-- Q2. Find Cal Ripken Jr.’s salary history.
--
-- - Sort by year in descending order.
-- - Your query should return a table with two columns, 
--   one for year and one for salary.
--
-- The "players" table contains the following columns:
--  "id", "first_name", "last_name", "bats", "throws", "weight",
--  "height", "debut", "final_game", "birth_year", "birth_month", 
--  "birth_day", "birth_city", "birth_state", and "birth_country"
-- 
-- -- Find Cal Ripken id
-- SELECT ROW_NUMBER() OVER (ORDER BY "last_name") AS i, "id", "first_name", "last_name"
-- FROM "players"
-- WHERE "first_name" LIKE 'Cal';
--
-- -- Result 16: 15726 | Cal | Ripken
--
-- The "salaries" table contains the following columns:
--  "id", "player_id", "team_id", "year" and "salary"
-- 
-- Answer:
SELECT "year", "salary" FROM "salaries"
WHERE "salaries"."player_id" = ( 
    SELECT "id" 
    FROM "players"
    WHERE "first_name" = 'Cal' AND "last_name" = 'Ripken')
ORDER BY "year" DESC;

-- Result: OK
-- 2 columns and 17 rows.