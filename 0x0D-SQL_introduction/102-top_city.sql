-- top three cities between july and agust
SELECT city, AVG(MAX(value)) AS avg_temp FROM temparetures WHERE month BETWEEN 7 AND 8 ORDER BY avg_temp DESC;
