-- Q12. Find the players among the 10 least expensive 
-- players per hit and among the 10 least expensive players per RBI in 2001.
--
-- - Your query should return a table with two columns, one for 
--   the players’ first names and one of their last names.
--
-- - You can calculate a player’s salary per RBI by dividing their 
--   2001 salary by their number of RBIs in 2001.
--
-- - You may assume, for simplicity, that a player will only 
--   have one salary and one performance in 2001.
--
-- - Order your results by player ID, least to 
--   greatest (or alphabetically by last name, as both are 
--   the same in this case!).
--
-- - Keep in mind the lessons you’ve learned in 10.sql and 11.sql!
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
SELECT "first_name", "last_name" FROM "players"
WHERE "players"."id" IN (
    SELECT "players"."id" FROM "players"
    JOIN "performances" ON "performances"."player_id" = "players"."id"
    JOIN "salaries" ON "salaries"."player_id" = "players"."id"
    WHERE "performances"."year" = 2001 
        AND "salaries"."year" = 2001
        AND "performances"."H" != 0
    ORDER BY ("salaries"."salary" / "performances"."H")
    LIMIT 10 
)
INTERSECT
SELECT "first_name", "last_name" FROM "players"
WHERE "players"."id" IN (
    SELECT "players"."id" FROM "players"
    JOIN "performances" ON "performances"."player_id" = "players"."id"
    JOIN "salaries" ON "salaries"."player_id" = "players"."id"
    WHERE "performances"."year" = 2001 
        AND "salaries"."year" = 2001
        AND "performances"."RBI" != 0
    ORDER BY ("salaries"."salary" / "performances"."RBI")
    LIMIT 10 
)
ORDER BY "last_name";

-- Result: OK
-- 2 columns and 6 rows