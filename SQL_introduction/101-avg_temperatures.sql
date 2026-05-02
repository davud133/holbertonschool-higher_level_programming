-- avarages
SELECT city, AVG(temperature) AS avg_temp FROM temperatures GROUP BY city ORDER BY temperature DESC
