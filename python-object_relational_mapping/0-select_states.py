#!/usr/bin/python3
"""Script that lists all states from database hbtn_0e_usa"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states')
    states = cursor.fetchall()

    for state in states:
        print(state)
