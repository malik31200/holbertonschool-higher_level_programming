#!/usr/bin/python3
"""
Lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    database = argv[3]

    connexion = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cur = connexion.cursor()

    cur.execute(
                """SELECT cities.id, cities.name, states.name
                FROM cities JOIN states
                ON cities.state_id = states.id
                ORDER BY cities.id ASC"""
    )

    for row in cur.fetchall():
        print(row)

    cur.close()
    connexion.close()
