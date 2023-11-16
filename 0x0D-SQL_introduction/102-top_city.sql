-- displays the top 3 average temp (F) by city ordered by temp desc
SELECT
    city,
    AVG(value) AS avg_temp
FROM temperatures
WHERE (month) IN (7, 8)
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;
