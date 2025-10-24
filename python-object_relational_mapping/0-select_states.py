#!/usr/bin/env python3
"""
lists all states from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # retrieve the arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

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
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    # Displaying results as tuples (id, name)
    for row in cur.fetchall():
        print(row)

    # Closing the cursor and connection
    cur.close
    connexion.close
