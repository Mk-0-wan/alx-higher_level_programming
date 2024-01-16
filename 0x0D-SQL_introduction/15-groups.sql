-- Grouping in Sql
SELECT score, COUNT(*) as number FROM second_table group by score order by score desc;
