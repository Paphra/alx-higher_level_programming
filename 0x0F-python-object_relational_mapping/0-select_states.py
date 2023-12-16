#!/usr/bin/python3
""" The selcect_states module

Contains the script to select all states from the database
"""

if __name__ == '__main__':
    import sys
    import MySQLdb

    host = 'localhost'
    port = 3306
    user, password, database = sys.argv[1:]
    db = MySQLdb.connect(
        host=host, port=port, user=user, password=password,
        database=database
    )
    cursor = db.cursor()
    query = "SELECT * FROM states ORDER BY states.id ASC"
    cursor.execute(query)
    results = cursor.fetchall()
    for state in results:
        print(state)

    cursor.close()
    db.close()
