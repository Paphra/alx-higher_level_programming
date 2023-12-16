#!/usr/bin/python3
""" The my_filter_states module

Contains the script to select all states from the database
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    host = 'localhost'
    port = 3306

    user, password, database, search = sys.argv[1:]
    db = MySQLdb.connect(
        host=host, port=port, user=user, password=password,
        database=database
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name='{}'\
        ORDER BY states.id ASC".format(search)
    cursor.execute(query)
    results = cursor.fetchall()
    for state in results:
        print(state)
    if len(results) == 0:
        print()

    cursor.close()
    db.close()
