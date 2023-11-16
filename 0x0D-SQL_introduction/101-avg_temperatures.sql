-- displays the average temp (F) by city ordered by temp desc
SELECT
    city,
    AVG(value) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC;
