-- Q1. Find the names and cities of 
-- all public schools in Massachusetts.
--
-- Answer:

SELECT "name", "city" FROM "schools"
WHERE "type" = 'Public School';

-- Result: OK
--  - 2 columns and 1,761 rows.