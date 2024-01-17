-- top three cities between july and agust
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE MAX(avg_temp) LIMIT July, Agust ORDER BY avg_temp DESC;
