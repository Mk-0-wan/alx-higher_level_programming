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

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)

    # create the city
    city = City(name='San Francisco')

    # create state
    state = State(name='California')

    # associate the state to the city
    state.related_cities.append(city)

    with Session.begin() as sn:
        sn.add(state)
