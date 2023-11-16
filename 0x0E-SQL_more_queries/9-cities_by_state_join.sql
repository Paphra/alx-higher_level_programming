-- lists all the cities contained in the database
SELECT cities.id, cities.name, states.name FROM cities JOIN states ON states.id ORDER BY cities.id;
