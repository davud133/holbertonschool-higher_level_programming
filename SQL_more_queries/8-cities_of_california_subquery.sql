-- gives cities
SELECT name FROM cities
WHERE id = state_id GROUP BY id ORDER BY id ASC;
