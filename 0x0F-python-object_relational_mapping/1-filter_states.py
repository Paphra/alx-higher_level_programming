#!/usr/bin/python3
""" The filter_states module

Contains the script to select all states from the database
"""

import sys
import MySQLdb

if __name__ == '__main__':

    host = 'localhost'
    port = 3306

    user, password, database = sys.argv[1:4]
    db = MySQLdb.connect(
        host=host, port=port, user=user, password=password,
        database=database
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name LIKE 'N%'\
        ORDER BY states.id ASC"
    cursor.execute(query)
    results = cursor.fetchall()
    for state in results:
        print(state)

    cursor.close()
    db.close()
