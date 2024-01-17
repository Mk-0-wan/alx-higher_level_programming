-- listing all the cities found in the hbtn_0d_usa database
-- First getting the names of the cities with the same foreign key
-- Then collecting all the name of the city is california
SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
