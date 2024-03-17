#!/usr/bin/python3

"""
A Script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
from sys import argv

def main():
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        name = argv[4]
    )

    cursor = db.cursor()
    the_query = cursor.execute("SELECT * FROM states where name = '{}' "
                                "ORDER BY id ASC").format(name)
    cusrsor.execute(the_query)

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()

if __name__ == '__main__':
    main()
