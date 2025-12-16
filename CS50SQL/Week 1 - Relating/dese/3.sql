-- Q3. Find the average per-pupil expenditure. 
-- Name the column “Average District Per-Pupil Expenditure”.
-- 
--  Note the `per_pupil_expenditure` column in the `expenditures` 
--  table contains the average amount, per pupil, each district 
--  spent last year. 
--  You’ve been asked to find the average of this set of averages,
--  weighting all districts equally regardless of their size.
--
-- Answer:
SELECT AVG("per_pupil_expenditure") 
AS "Average District Per-Pupil Expenditure"
FROM expenditures;

-- Result: OK
-- -  1 column and 1 row.