#!/usr/bin/python3
"""
script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
"""

import MySQLdb
import sys


def filter_states(username, password, db_name):
    """List states with names starting with 'N'."""
    db = MySQLdb.connect(host='localhost', port=3306,
                         user=username, passwd=password, db=db_name)

    cursor = db.cursor()

    query = "SELECT DISTINCT * " \
        "FROM states " \
        "WHERE name LIKE 'N%' " \
        "ORDER BY id ASC"
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    filter_states(username, password, db_name)
