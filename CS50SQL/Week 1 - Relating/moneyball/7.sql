-- Q7. Find the name of the player who’s been paid the highest salary,
-- of all time, in Major League Baseball.
--
-- - Your query should return a table with two columns, one for 
--   the player’s first name and one for their last name.
--
-- The "players" table contains the following columns:
--  "id", "first_name", "last_name", "bats", "throws", "weight",
--  "height", "debut", "final_game", "birth_year", "birth_month", 
--  "birth_day", "birth_city", "birth_state", and "birth_country"
--
-- The "salaries" table contains the following columns:
--  "id", "player_id", "team_id", "year" and "salary"
--
-- Answer:
SELECT "first_name", "last_name"
FROM "players"
WHERE "id" = (
    SELECT "player_id" 
    FROM "salaries"
    WHERE "salary" = (
        SELECT MAX("salary")
        FROM "salaries"
    )
);

-- Result: OK
-- 2 columns and 1 row.