#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa"""
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         password=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("""SELECT cities.id, cities.name, states.name
                   FROM cities JOIN states ON cities.state.id = states.id
                   ORDER BY cities.id;
                   """)
    cities = cursor.fetchall()

    for city in cities:
        print(city)
