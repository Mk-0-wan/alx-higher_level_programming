#!/usr/bin/python3
"""Making a simple connection, and innerjoining two tables to retrive data"""

if __name__ == '__main__':

    import MySQLdb as mdb
    import sys

    # first set up the connection configuration
    database_config = {
        'host': 'localhost',
        'port': 3306,
        'user': sys.argv[1],
        'password': sys.argv[2],
        'database': sys.argv[3]
    }

    # with block will automatically close both the database and the cursor
    # once the with block is exited
    try:
        with mdb.connect(**database_config) as db:
            with db.cursor() as cur:
                query = "SELECT cities.id, cities.name, states.name FROM\
                     cities INNER JOIN states ON cities.state_id = states.id\
                     ORDER BY cities.id ASC"
                cur.execute(query)
                for row in cur.fetchall():
                    print(row)
    except mdb.Error as e:
        raise (e)
