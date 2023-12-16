#!/usr/bin/python3
""" The my_filter_states module

Contains the script to select all states from the database
"""

import sys
import MySQLdb

if __name__ == '__main__':
    host = 'localhost'
    port = 3306

    user, password, database, search = sys.argv[1:5]
    db = MySQLdb.connect(
        host=host, port=port, user=user, password=password,
        database=database
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE BINARY name='{}'\
        ORDER BY states.id ASC".format(search)
    cursor.execute(query)
    results = cursor.fetchall()
    for state in results:
        print(state)

    cursor.close()
    db.close()
