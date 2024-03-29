#!/usr/bin/python3
"""Making a simple connection, and parsing the name of the state to retrive"""

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
                select_query = "SELECT states.id, states.name FROM states\
                     WHERE BINARY states.name LIKE '%{0}%'\
                     ORDER BY states.id ASC".format(sys.argv[4])
                cur.execute(select_query)
                for row in cur.fetchall():
                    print(row)
    except mdb.Error as e:
        raise (e)
