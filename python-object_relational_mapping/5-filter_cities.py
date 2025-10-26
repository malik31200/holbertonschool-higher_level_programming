#!/usr/bin/python3
"""
takes in the name of a state as an argument
lists all cities of that state, using the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]
    state_name = argv[4]

    connexion = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = connexion.cursor()

    cur.execute(
        """SELECT cities.name
        from cities
        JOIN states
        ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC""",
        (state_name,)
    )

    for row in cur.fetchall():
        print(row)
    cur.close()
    connexion.close()
