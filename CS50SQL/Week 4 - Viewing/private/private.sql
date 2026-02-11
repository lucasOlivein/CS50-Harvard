-- Task: decode the cipher
--   ----------------------
--   | 14 	    98  	4   |
--   | 114 	    3 	    5   |
--   | 618  	72 	    9   |
--   | 630  	7 	    3   |
--   | 932 	    12 	    5   |
--   | 2230 	50 	    7   |
--   | 2346 	44 	    10  |
--   | 3041 	14 	    5   |
--   ------------------------
-- Each triplet is structured as follows:

    -- - The first number in the triplet is the sentence number referenced by the encoder.
    -- - The second number in the triplet is the character number, within that sentence, at which the message begins.
    -- - The third number in the triplet is the message length in characters (i.e., how many characters to read from the first, including spaces and punctuation).

-- At the end of your process you should have a view structured as follows:

    -- - The view should be named `message`
    -- - The view should have a single column, `phrase`
    -- - When the following SQL query is executed on `private.db`, 
    --   your view should return a single column in which each row is one phrase in the message. 

-- In private.sql, you should write all SQL statements required to replicate your creation of the view. That is:

    -- - If creating the view requires creating a separate table and inserting data into it, 
    --   you should ensure that private.sql contains the statements to create that table and 
    --   insert that data. (Don’t be afraid to add tables and add data as you wish!)
    -- - `private.sql`, when run a fresh instance of `private.db`, should be able to fully reconstruct your view.


CREATE VIEW "message" AS
WITH "phrases" AS (
    SELECT substr("sentence", 98, 4) AS "phrase" FROM sentences WHERE "id" = 14
    UNION ALL
    SELECT substr("sentence", 3, 5) FROM sentences WHERE "id" = 114
    UNION ALL
    SELECT substr("sentence", 72, 9) FROM sentences WHERE "id" = 618
    UNION ALL
    SELECT substr("sentence", 7, 3) FROM sentences WHERE "id" = 630
    UNION ALL
    SELECT substr("sentence", 12, 5) FROM sentences WHERE "id" = 932
    UNION ALL
    SELECT substr("sentence", 50, 7) FROM sentences WHERE "id" = 2230
    UNION ALL
    SELECT substr("sentence", 44, 10) FROM sentences WHERE "id" = 2346
    UNION ALL
    SELECT substr("sentence", 14, 5) FROM sentences WHERE "id" = 3041
) 
SELECT "phrase" FROM "phrases"; 