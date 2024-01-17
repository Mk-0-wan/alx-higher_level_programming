-- top three cities between july and agust
SELECT city, avg_temp FROM ( SELECT city, AVG(value) as avg_temp FROM temperatures WHERE month = 7 OR month = 8 GROUP BY city ORDER BY AVG(value) DESC) results LIMIT 3;
