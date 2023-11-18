#!/usr/bin/python3
""" script that takes in arguments and displays all values in the 
states table of hbtn_0e_0_usa where name matches
the argument. But this time, write one that is safe from MySQL injections!
"""

import MySQLdb
import sys from argv

if __name__ == '__main__':
    """
    Access to the database to list the states
    """
    db = MySQldb.connect(host="localhost", user=argv[1], port=3306, 
            passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("select * from states \
                where name like binary $(name)s \
                order by states.id" {
                    'name': argv[4]
                    })
        rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
