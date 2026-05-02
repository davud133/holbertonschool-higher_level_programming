-- avarages
SELECT name, AVG(temperature) FROM temperatures GROUP BY name ORDER BY temperature DESC
