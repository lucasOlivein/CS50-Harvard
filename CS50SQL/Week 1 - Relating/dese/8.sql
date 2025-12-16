-- Q8. Display the names of all school districts and the number
-- of pupils enrolled in each.
--
--  The "districts" table contains the following columns:
--      "id", "name", "type", "city", "state" and "zip".
--
--  The "expenditures" table contains the following columns:
--      "id", "district_id", "pupils", "per_pupil_expenditure"
--
-- - "pupils": is the number of pupils attending the given district.
--
-- Answer:
SELECT "name", "pupils"
FROM "districts" 
JOIN "expenditures" ON "districts"."id" = "expenditures"."district_id";

-- Result: OK
-- - 2 columns and 396 rows.