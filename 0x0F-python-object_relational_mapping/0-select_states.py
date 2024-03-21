#!/usr/bin/python3

"""
A Script that lists all states from the database hbtn_0e_0_usa
Parameters for script: mysql username, mysql password, database name
It must use the `MySQLdb` module
Script should connect to a MySQL server runnimg on `localhost` at port `3306`
Results must be in ascending order by `states.id`.
Code should not be executed when imported.
"""

import MySQLdb
from sys import argv


def main():
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == '__main__':
    main()
