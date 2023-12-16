#!/usr/bin/python3
""" cities_by_state module

a script that lists all cities from the database hbtn_0e_4_usa
"""

import sys
import MySQLdb


def list_all_cities(user, pw, db):
    """ The function to retrieve all cities by state
    """

    db = MySQLdb.connect(
        host='localhost', port=3306,
        user=user, password=pw, database=db
    )
    cursor = db.cursor()
    query = """
        SELECT cities.id, cities.name, states.name FROM cities
        JOIN states ON cities.state_id=states.id
        ORDER BY cities.id ASC
    """

    cursor.execute(query)
    results = cursor.fetchall()

    for city in results:
        print(city)

    cursor.close()
    db.close()


if __name__ == '__main__':
    user, password, database = sys.argv[1:4]

    list_all_cities(user, password, database)
