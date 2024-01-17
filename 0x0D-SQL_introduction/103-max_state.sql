-- Max temp of each state
SELECT state, MAX(value) AS max_temp FROM temparetures GROUP BY state ORDER BY max_temp ASC;
