-- Lists all records in the table second_table with score >= 10.
-- Records are in descending order of score.
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
