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
    # make a list of all the queries to try
    # include the left join right join full and inner join

    select_queirs = [
        "SELECT cities.id, cities.name, states.name FROM cities INNER JOIN\
         states ON cities.state_id = states.id WHERE BINARY states.name LIKE\
         ORDER BY cities.id ASC",

        "SELECT cities.id, cities.name, states.name FROM cities LEFT JOIN\
         states ON cities.state_id = states.id WHERE BINARY states.name LIKE\
         ORDER BY cities.id ASC",

        "SELECT cities.id, cities.name, states.name FROM cities RIGHT JOIN\
         states ON cities.state_id = states.id WHERE BINARY states.name LIKE\
         ORDER BY cities.id ASC",
    ]

    # with block will automatically close both the database and the cursor
    # once the with block is exited
    try:
        with mdb.connect(**database_config) as db:
            with db.cursor() as cur:
                for query in select_queries:
                    try:
                        cur.execute(query, ('%' + sys.argv[4] + '%',))
                        cur_rows = cur.fetchall()
                        if (cur_rows):
                            for indx, row in enumerate(cur_rows):
                                print(row[1], end=("\n", ",")
                                      [(indx + 1) < len(cur_rows)])
                        else:
                            print()
                        break
                    except mdb.Error as e:
                        continue
    except mdb.Error as e:
        raise (e)
