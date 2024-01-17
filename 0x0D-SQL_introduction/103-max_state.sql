-- Max temp of each state
SELECT state, MAX(value) AS max_temp FROM temparetures ORDER BY state ASC;
