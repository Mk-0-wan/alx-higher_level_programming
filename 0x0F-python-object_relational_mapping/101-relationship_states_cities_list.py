#!/usr/bin/python3
""" Making a simple association between two tables"""
import sys
from relationship_state import State, Base
from relationship_city import City
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

    # select the whole state table
    result = sn.query(State).all()

    if (result):
        for state in result:
            print(f"{state.id}: {state.name}")
            # use the cities attribute which has a list of all the city objects
            for city in state.cities:
                print(f"\t{city.id}: {city.name}")
