#!/usr/bin/python3
"""
Script to print all name starting with 'N' from database
hbtn_0e_0_usa
"""

import MySQLdb
import sys from argv

if __name__ == '__main__':
    """
    Access to the database to list the name of states starting
    with 'N'
    """

    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
            passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("select * from states \
            where name like binary 'N%' \
            order by states.id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)
