-- Q3. Find Ken Griffey Jr.’s home run history.
--
-- - Sort by year in descending order.
-- - Note that there may be two players with the name “Ken Griffey.” 
--   - This Ken Griffey was born in 1969.
-- - Your query should return a table with two columns:
--   - one for year and
--   - one for home runs.
--
-- The "players" table contains the following columns:
--  "id", "first_name", "last_name", "bats", "throws", "weight",
--  "height", "debut", "final_game", "birth_year", "birth_month", 
--  "birth_day", "birth_city", "birth_state", and "birth_country"
--
-- -- Find Ken Griffey who was born in 1969.
-- SELECT ROW_NUMBER() OVER (ORDER BY "birth_year") AS i, "id", "first_name", "last_name", "birth_year"
-- FROM "players"
-- WHERE "first_name" = 'Ken' AND "last_name" = 'Griffey';
-- 
-- Result 2: 7266 | Ken | Griffey | 1969
--
-- The "performances" table contains the following columns:
--  "id", "player_id", "team_id", "year", "G", "AB", "H",
--  "2B", "3B", "HR", "RBI", "SB"
--
-- Answer:
SELECT "year", "HR"
FROM "performances"
WHERE "player_id" = (
    SELECT "id" 
    FROM "players"
    WHERE "first_name" = 'Ken' 
    AND "last_name" = 'Griffey' 
    AND "birth_year" = 1969
)
ORDER BY "year" DESC;

-- Result: OK
-- 2 columns and 13 rows.