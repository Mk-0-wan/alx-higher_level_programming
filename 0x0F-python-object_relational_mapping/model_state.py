#!/usr/bin/python3
"""Translating a python class object and mapping it to a mysql database"""
from sqlalchemy import String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class state which inherits from the Base(declerative_base) in order
    to make a simple connection to the database in order to make the table from
    this class instance

    Args:
        __tablename__ (class  instance attribute): holds the table name
        id(integer): this will be translated to the id column in the sql table
        name(string): this will be translated to the name column in the sql
    """
    __tablename__ = 'states'

    # setting up the id properties
    id = Column(
        'id',
        Integer(11),
        primary_key=True,
        autoincrement=True,
        nullable=False,
        unique=True
    )

    # setting up the name properties
    name = Column(
        'name',
        String(128),
        nullable=False
    )
