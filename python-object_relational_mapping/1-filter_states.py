#!/usr/bin/python3
"""Script lists all states with a name starting with N from database
hbtn_0e_0_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.arv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.excecute("SELECT * FROM states ORDER BY id")
    states = cursor.fetchall()

    for state in states:
        if state[1][0] == 'N':
            print(state)
