#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa filtered by
   name supplied in argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    pointer = database.cursor()
    args = sys.argv[4]
    pointer.execute("SELECT * FROM states WHERE name LIKE %s", (args, ))
    rows = pointer.fetchall()
    for row in rows:
        print(row)
    pointer.close()
    database.close()
