-- Checking for all null values and skipping them
SELECT score, name FROM second_table WHERE name IS NOT NULL order by score desc;
