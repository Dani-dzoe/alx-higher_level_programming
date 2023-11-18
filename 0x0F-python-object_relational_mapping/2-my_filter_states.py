#!/usr/bin/python3

"""
Script that takes in an argument and displays all values in the states 
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys from argv

if __name__ == '__main__':
    """
    Access the databases to list the states
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306, passwd=argv[2], db=argv[3])

    cur = db.cursor()
    cur.execute("select * from states \
            where name like binary '{}' \
            order by states ASC".format(argv[4]))
    rows = cur.fetchall()

    for row in rows:
        print(row)
