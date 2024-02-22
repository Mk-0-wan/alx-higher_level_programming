#!/usr/bin/python3
"""Translating a python class object and mapping it to a relational
mysql database"""
from model_state import Base, State
from sqlalchemy import Column, String, Integer, ForeignKey


class Cities(Base):
    """Class Cities, inherits from the Base class, citites will be having a
    relationship with the state id as it's foreign key values

    Args:
        __tablename__ (class  instance attribute): holds the table name
        id(integer): this will be translated to the id column in the sql table
        name(string): this will be translated to the name column in the sql
    """
    __tablename__ = 'cities'

    # setting up the id properties
    id = Column(
        'id',
        Integer,
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True
    )

    # key part of the relationship database between states and cities
    state_id = Column(
        'state_id',
        ForeignKey('states.id')
    )

    # setting up the name properties
    name = Column(
        'name',
        String(128),
        nullable=False
    )

    def __init__(self, name):
        """Initializes the class cities name to allow creation of uniqe objects
        to the database"""
        self.name = name
