-- Lists the number of records in the second_table for each score, ordered by the number of records in descending order.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
