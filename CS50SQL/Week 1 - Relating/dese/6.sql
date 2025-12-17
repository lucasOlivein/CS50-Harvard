-- Q6. Find the names of schools (public or charter!) that
-- reported a 100% graduation rate.
--
--  The "schools" table contains the following columns:
--      "id", "district_id", "name", "type", "city", 'state' and "zip".
--
--  The "graduation_rates" table contains the following columns:
--      "id", "school_id", "graduated", "dropped" and "excluded".
--
-- Answer:

SELECT "name" FROM "schools"
WHERE "id" IN (
    SELECT "school_id" 
    FROM "graduation_rates"
    WHERE "graduated" = 100);

-- Result: OK
-- - 1 column and 9 rows.
