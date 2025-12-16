-- Q13. Answer a question you have about the data! The query should:
--  - Involve at least one JOIN or subquery
--
--      Q. Analyze the relationship between school dropout rates
--      and negative teacher evaluation rates at the district level.
--      Schools with:
--      - an above-average percentage of students who dropped out before graduation
--      In districts with:
--      - an above-average percentage of teachers rated as "needs improvement"
--      - an above-average percentage of teachers rated as "unsatisfactory"
--
-- Schools with an above-average dropout rate.
-- SELECT "name" FROM "schools"
-- JOIN "graduation_rates" ON "schools"."id" = "graduation_rates"."school_id"
-- WHERE "dropped" > (
--     SELECT AVG("dropped") FROM "graduation_rates"
-- );

-- Districts with above-average percentage rates of:
--  - "Needs Improvement"
--  - "Unsatisfactory"
-- SELECT "name", ("needs_improvement" + "unsatisfactory")/2 AS "avg_negative_rate" FROM "districts"
-- JOIN "staff_evaluations" ON "districts"."id" = "staff_evaluations"."district_id"
-- WHERE "avg_negative_rate" > (
--     SELECT (AVG(needs_improvement) + AVG(unsatisfactory))/2 
--     FROM "staff_evaluations"
-- )
-- ORDER BY "avg_negative_rate" DESC;

-- Answer:
-- Schools with an above-average dropout rate
-- located in districts with an above-average negative evaluation rate.
SELECT "schools"."name" AS "School", "dropped" AS "Drop Rate" ,("needs_improvement" + "unsatisfactory")/2 AS "Avg negative rate"
FROM "schools" 
JOIN "staff_evaluations" ON "schools"."district_id" = "staff_evaluations"."district_id"
JOIN "graduation_rates" ON "schools"."id" = "graduation_rates"."school_id"
WHERE "Avg negative rate" > (
    SELECT (AVG(needs_improvement) + AVG(unsatisfactory))/2 
    FROM "staff_evaluations"
) AND "dropped" > (
    SELECT AVG("dropped") FROM "graduation_rates"
)
ORDER BY "Drop Rate" DESC;