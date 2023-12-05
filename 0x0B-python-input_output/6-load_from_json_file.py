#!/usr/bin/python3
"""Json format"""
import json


def load_from_json_file(filename):
    """Performs a diserialization process

    Args:
        my_obj (str): a python string object

    Return:
         a json formatted data from python string object
    """
    with open(filename, "r", encoding="utf-8") as fp:
       x = json.load(fp)
    return x
