#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
Where name start with N
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # retrieve the arguments
    username = argv[1]
    password = argv[2]
    database_name = argv[3]

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

    # Executing SQL query to retrieve all states
    cur.execute(
                "SELECT * FROM states"
                "WHERE name LIKE BINARY 'N%'"
                "ORDER BY id ASC")

    # Displaying results as tuples (id, name)
    for row in cur.fetchall():
        print(row)

    # Closing the cursor and connection
    cur.close
    connexion.close
