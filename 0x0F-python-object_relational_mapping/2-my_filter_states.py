#!/usr/bin/python3
""" The my_filter_states module

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
    query = sys.argv[4]
    db = MySQLdb.connect(
        host=host, port=port, user=user, password=password,
        database=database
    )
    db.query(
        "SELECT * FROM states WHERE name='{}' ORDER BY states.id ASC".format(
            query
        )
    )
    result = db.store_result()
    for state in result.fetch_row(maxrows=0):
        print(state)
