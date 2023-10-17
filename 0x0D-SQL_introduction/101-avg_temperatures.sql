-- script that displays the average temperature by city ordered by temperature
-- The column for the average is labeled avg_temp
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
