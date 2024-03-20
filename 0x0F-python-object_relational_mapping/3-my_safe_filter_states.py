#!/usr/bin/python3

"""
A Script that displays all values in the states table of hbtn_0e_0_usa
where name matches the provided argument
"""

import MySQLdb
from sys import argv


def main():
    if len(argv) != 5:
        print("Usage: {} <username> <password> <database> <state_name>".format(
            argv[0]))
        exit()

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cursor.execute(query, (argv[4],))

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
