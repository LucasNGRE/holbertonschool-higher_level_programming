-- Lists the number of records in the second_table for each score, ordered by the number of records in descending order.
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;
