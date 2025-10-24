#!/usr/bin/python3
"""
A script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # retrieve the arguments
    username = argv[1]
    password = argv[2]
    database_name = argv[3]
    state_name_searched = argv[4]

    # connect to Mysl database
    connexion = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name
    )

    # Create a cursor
    cur = connexion.cursor()

    # Executing SQL query with format
    cur.execute(
                "SELECT * FROM states "
                "WHERE BINARY states.name = '{}' "
                "ORDER BY states.id ASC".format(state_name_searched)
                )

    # Displaying results as tuples (id, name)
    for row in cur.fetchall():
        print(row)

    # Closing the cursor and connection
    cur.close
    connexion.close
