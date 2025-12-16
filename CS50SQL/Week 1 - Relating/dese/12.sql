-- Q12. Find public school districts with:
-- -  above-average per-pupil expenditures and
-- -  an above-average percentage of teachers rated “exemplary”. 
-- Your query should return:
-- -  the districts’ names, along with 
-- -  their per-pupil expenditures and
-- -  percentage of teachers rated exemplary. 
-- Sort the results first
-- -  by the percentage of teachers rated exemplary (high to low), 
-- -  then by the per-pupil expenditure (high to low).
--
--  The "districts" table contains the following columns:
--      "id", "name", "type", "city", "state" and "zip".
--
--  The "expenditures" table contains the following columns:
--      "id", "district_id", "pupils", "per_pupil_expenditure"
--
--  The "staff_evaluations" table contains the following columns:
--      "id", "district_id", "evaluated", "exemplary", "proficient",
--      "needs_improvement" and "unsatisfactory"
--
--      "exemplary" represents the percentage (0–100) of district staff
--       evaluated as "exemplary".
--
-- Answer:
SELECT "name", "per_pupil_expenditure", "exemplary"
FROM "districts"
JOIN "expenditures" ON "districts"."id" = "expenditures"."district_id"
JOIN "staff_evaluations" ON "districts"."id" = "staff_evaluations"."district_id"
WHERE "type" = 'Public School District' 
AND "per_pupil_expenditure" > (
    SELECT AVG("per_pupil_expenditure") FROM "expenditures"
) AND "exemplary" > (
    SELECT AVG("exemplary") FROM "staff_evaluations"
)
ORDER BY "exemplary" DESC, "per_pupil_expenditure" DESC;

-- Result: OK
-- - 3 columns and 65 rows.