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
                select_query = "SELECT cities.id, cities.name, states.name\
                     FROM cities INNER JOIN states ON\
                     cities.state_id = states.id\
                     WHERE BINARY states.name LIKE %s\
                     ORDER BY cities.id ASC"
                cur.execute(select_query, ('%' + sys.argv[4] + '%',))
                cur_rows = cur.fetchall()
                for indx, row in enumerate(cur_rows):
                    print(row[1],
                          end=("\n", ",")[(indx + 1) < cur_rows.__len__()])
    except mdb.Error as e:
        raise (e)
