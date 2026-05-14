-- list all cities
SELECT id, name state.name FROM cities JOIN states ON cities.state_id = state.id;
