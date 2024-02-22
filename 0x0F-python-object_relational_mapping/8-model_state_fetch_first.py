#!/usr/bin/python3
"""Start a connections and ping to check if it's true, then make a session obj
which will allow us to make some query to the database
Querying for the first object returned
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

    # Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    sn = Session()
    result = sn.query(State).first()
    print(str(result.id) + ': ' + result.name)
