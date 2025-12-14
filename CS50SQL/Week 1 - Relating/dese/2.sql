-- Q2. Find the names of districts that are no longer operational.
--
--  Districts that are no longer operational have 
--  “(non-op)” at the end of their name.
--
-- Answer:
SELECT "name", COUNT(*) FROM "districts"
WHERE "name" LIKE '%(non-op)';

-- Result: OK
--  - 1 column and 121 rows.