-- list all cities
USE hbtn_0d_usa
SELECT id, name state.name FROM cities JOIN states ON cities.state_id = state.id;
