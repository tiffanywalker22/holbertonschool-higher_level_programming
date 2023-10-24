#!/usr/bin/python3
""" Script that takes in arguments and displays all values in states
table of hbtn_0e_0_usa where name matches argument,
safe from mysql injections"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s ORDER BY id",
                   (sys.argv[4],))
    states = cursor.fetchall()

    for state in states:
        if state[1] == sys.argv[4]:
            print(state)
