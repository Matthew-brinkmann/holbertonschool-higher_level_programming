-- lists all records of the table second_table score >= 10
-- display both the score and the name (in this order)
-- Records should be ordered by score (top first)
-- DB will be passed as an argument
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
