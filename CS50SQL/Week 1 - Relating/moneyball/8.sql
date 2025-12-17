-- Q8. Find the 2001 salary of the player who hit the most home runs in 2001.
--
-- - Your query should return a table with one column, the salary of the player.
-- 
-- The "salaries" table contains the following columns:
--  "id", "player_id", "team_id", "year" and "salary"
-- 
-- The "performances" table contains the following columns:
--  "id", "player_id", "team_id", "year", "G", "AB", "H",
--  "2B", "3B", "HR", "RBI", "SB"
--
-- Answer:
SELECT "salary"
FROM "salaries"
WHERE "player_id" = (
    SELECT "player_id"
    FROM "performances"
    WHERE "HR" = (
        SELECT MAX("HR") FROM "performances"
        WHERE "year" = 2001
    )
)
AND "year" = 2001;

-- Result: OK
-- 1 column and 1 row.