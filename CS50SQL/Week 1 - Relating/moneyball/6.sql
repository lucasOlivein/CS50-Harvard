-- Q6. Find the top 5 teams, sorted by the total 
-- number of hits by players in 2001.
--
-- - Call the column representing total hits by players
--   in 2001 “total hits”.
-- - Sort by total hits, highest to lowest.
-- - Your query should return two columns, 
--   one for the teams’ names and one for their total hits in 2001.
--
-- The "teams" table contains the following columns:
--  "id", "year", "name", "park"
--
-- The "performances" table contains the following columns:
--  "id", "player_id", "team_id", "year", "G", "AB", "H",
--  "2B", "3B", "HR", "RBI", "SB"
--
-- Answer:
SELECT "name", COUNT("H") AS "total hits"
FROM "performances"
JOIN "teams" ON "performances"."team_id" = "teams"."id"
GROUP BY "teams"."id"
ORDER BY "total hits" DESC
LIMIT 5;

-- Result: OK
-- 2 columns and 5 rows.