#!/usr/bin/python3
""" The selcect_states module

Contains the script to select all states from the database
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    host = 'localhost'
    port = 3306
    user = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    db = MySQLdb.connect(
        host=host, port=port, user=user, password=password,
        database=database
    )
    db.query(
        "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"
    )
    result = db.store_result()
    for state in result.fetch_row(maxrows=0):
        print(state)
