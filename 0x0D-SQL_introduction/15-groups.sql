-- lists the number of records with the same score in the table second_table
-- the result should display: the score
-- the number of records for this score with the label number
-- DB will be passed as an argument
SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
