#!/usr/bin/python3
"""Lists all cities associated with a state passed as an argument
   from the database hbtn_0e_4_usa filtered.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    pointer = database.cursor()
    pointer.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = pointer.fetchall()
    tempList = list(row[0] for row in rows)
    print(*tempList, sep=", ")
    pointer.close()
    database.close()
