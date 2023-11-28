#!/usr/bin/python3
"""Greetings from Python3"""

def say_my_name(first_name, last_name=""):
    """A python function that prints out the names
    passed as arguments

    Args:
        first_name (string): string rep for the person first name
        last_name (string): string rep for the person last name

    Return:
        greeting sentence to introduce a person with the given names
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
