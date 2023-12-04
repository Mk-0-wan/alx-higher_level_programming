#!/usr/python3
"""
Listing all the attributes of an object
"""


def lookup(obj) -> list:
    """List out all the builtin attributes of an object"""
    return dir(obj)
