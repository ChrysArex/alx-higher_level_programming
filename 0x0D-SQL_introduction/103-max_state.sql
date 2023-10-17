-- script that displays the max temperature of each state
-- The database name must be passed in the commande
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state;
