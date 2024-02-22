#!/usr/bin/python3
"""Start a connections and ping to check if it's true, then make a session obj
which will allow us to make some query to the database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb'
        '://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True
    )

    # Setting the database table the same as the class object structure
    Base.metadata.create_all(engine)

    # Making a connection that will allow effective changes to the database
    Session = sessionmaker(bind=engine)

    # We need to make a class so that we can use multiple objects from sn

    # Making the objects that will be inserted to the table
    state_obj = State("Louisiana")

    # this will consolidate for .begin(), .rollback(), .commit()
    count = 0
    with Session.begin() as sn:
        sn.add(state_obj)
        count = sn.query(State).count()
    print(count)
