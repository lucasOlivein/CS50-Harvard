-- Q11. Display:
-- - the names of schools, 
-- - their per-pupil expenditure, and 
-- - their graduation rate. 
-- Sort the schools from: 
--  - greatest per-pupil expenditure to least. 
-- If two schools have the same per-pupil expenditure, sort by school name.
--
-- You should assume a school spends the same amount per-pupil
-- their district as a whole spends.
--
--  The "schools" table contains the following columns:
--      "id", "district_id", "name", "type", "city", 'state' and "zip".
--
--  The "expenditures" table contains the following columns:
--      "id", "district_id", "pupils", "per_pupil_expenditure"
-- 
--  The "graduation_rates" table contains the following columns:
--      "id", "school_id", "graduated", "dropped" and "excluded".
--
-- Answer:
SELECT "name", "per_pupil_expenditure", "graduated"
FROM "schools" 
JOIN "expenditures" ON "schools"."district_id" = "expenditures"."district_id"
JOIN "graduation_rates" ON "schools"."id" = "graduation_rates"."school_id"
ORDER BY "per_pupil_expenditure" DESC, "name" ASC;

-- Result: OK
-- - 3 columns and 391 rows.