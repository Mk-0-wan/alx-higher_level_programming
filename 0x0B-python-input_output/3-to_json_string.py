#!/usr/bin/python3
"""Json format"""
import json


def to_json_string(my_obj):
    """Performs a serialization process

    Args:
        my_obj (str): a python string object

    Return:
         a json formatted data from python string object
    """
    return (json.dumps(my_obj))
