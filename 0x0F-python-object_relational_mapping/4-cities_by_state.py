#!/usr/bin/pythn3
"""
script that lists all cities from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys from argv

if __name__ == '__main__':
    """
    Access to the database to list all cities
    """
    db = MySQLdb.connect(host="localhost", user=argv[1], port=3306, 
            passwd=argv[2], db=argv[3])

    with db.cursor() as cur:
        cur.execute("""
        select
            cities.id, cities.name, states.name
        form 
            cities.id
        join
            states
        on
            city.state_id = states.id
        order by
            cities.id ASC
        """)

        rows = cur.fetchall()

    if rows is not None:
        for row in rows:
            print(row)
