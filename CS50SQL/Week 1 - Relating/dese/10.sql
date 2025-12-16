-- Q10. Find the 10 **public school districts** with the highest
-- per-pupil expenditures. Your query should return the **names of the
-- districts** and the **per-pupil expenditure** for each.
--
--  The "districts" table contains the following columns:
--      "id", "name", "type", "city", "state" and "zip".
--
--  - type: denotes the type of district, wich can be “Public School District” or
--    “Charter District”
--
--  The "expenditures" table contains the following columns:
--      "id", "district_id", "pupils", "per_pupil_expenditure"
--
--  - "per_pupil_expenditure": is the amount of money spent, in dollars,
--     on each student attending the district
--
-- Answer:
SELECT "name", "per_pupil_expenditure"
FROM "districts" 
JOIN "expenditures" ON "districts".id = "expenditures"."district_id"
WHERE "districts"."type" = 'Public School District'
ORDER BY "per_pupil_expenditure" DESC
LIMIT 10;

-- Result: OK
-- - 2 columns and 10 rows.