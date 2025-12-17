-- Q4. Find the 10 cities with the most public schools. 
-- Your query should return:
--  - the names of the cities and 
--  - the number of public schools within them, 
-- ordered from:
--  - greatest number of public schools to least. 
-- If two cities have the same number of public schools, 
-- order them alphabetically.
--
-- Answer:

SELECT "city", COUNT("city") AS "public school number" FROM "schools"
GROUP BY "city"
HAVING "type" = 'Public School'
ORDER BY "public school number" DESC, "city" ASC
LIMIT 10;

-- Result: OK
-- - 2 columns and 10 rows.
--
-- Explanation:
--  The "schools" table contains the following columns:
--      "id", "district_id", "name", "type", "city", "state" and "zip"
--  Therefore, it is possible to count how many schools there are in a city
--  by counting how many times a specific city name appears
--  in the "city" column of the schools table.