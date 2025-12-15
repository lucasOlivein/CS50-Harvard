-- Q9. Find the name (or names) of the school district(s) with
-- the single least number of pupils. Report only the name(s).
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
SELECT "name" FROM districts
JOIN "expenditures" ON "districts"."id" = "expenditures"."district_id"
WHERE "pupils" = (
    SELECT MIN("pupils") FROM "expenditures"
);

-- Result: OK
-- - 1 column and 1 row.