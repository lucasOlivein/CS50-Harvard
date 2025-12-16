-- Q5. Find all teams that Satchel Paige played for.
-- 
-- - Your query should return a table with a single column,
--   one for the name of the teams.
--
-- The "players" table contains the following columns:
--  "id", "first_name", "last_name", "bats", "throws", "weight",
--  "height", "debut", "final_game", "birth_year", "birth_month", 
--  "birth_day", "birth_city", "birth_state", and "birth_country"
--
-- -- Find Satchel Paige id
-- SELECT "id", "first_name", "last_name"
-- FROM "players"
-- WHERE "first_name" = 'Satchel' AND "last_name" = 'Paige';
--
-- Result: 14190 | Satchel | Paige
--
-- The "teams" table contains the following columns:
--  "id", "year", "name", "park"
--
-- The "performances" table contains the following columns:
--  "id", "player_id", "team_id", "year", "G", "AB", "H",
--  "2B", "3B", "HR", "RBI", "SB"
--
-- Answer:
SELECT "name" FROM "teams"
WHERE "teams"."id" IN (
    SELECT "team_id" FROM "performances"
    WHERE "player_id" = (
        SELECT "id" FROM "players"
        WHERE "first_name" = 'Satchel' AND "last_name" = 'Paige'
    )
);

-- Result: OK
-- 1 column and 3 rows.