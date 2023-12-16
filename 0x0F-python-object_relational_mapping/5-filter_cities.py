#!/usr/bin/python3
""" filter_cities module

a script that lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb


def list_cities_of_state(user, pw, db, state):
    """ The function to retrieve all cities by state
    """

    db = MySQLdb.connect(
        host='localhost', port=3306,
        user=user, password=pw, database=db
    )
    cursor = db.cursor()
    query = """
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id=states.id
        WHERE states.name=%s
        ORDER BY cities.id ASC
    """
    params = (state,)

    cursor.execute(query, params)
    results = cursor.fetchall()

    cities = ''
    for city in results:
        if (cities == ''):
            cities += city[0]
        else:
            cities += ', {}'.format(city[0])
    print(cities)

    cursor.close()
    db.close()


if __name__ == '__main__':
    user, password, database, state = sys.argv[1:5]

    list_cities_of_state(user, password, database, state)
