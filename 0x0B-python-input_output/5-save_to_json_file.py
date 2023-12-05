#!/usr/bin/python3
"""Writing to a json file"""
import json


def save_to_json_file(my_obj, filename):
    """Writing to a file and returns the number char written

   Args:
        filename (str):name of the file to write to
        my_obj (str): input data to be written which is a python
        string object
    Return:
        number of chars written by the user
    """
    try:
        with open(filename, "w", encoding="utf-8") as fp:
            fp.write(json.dumps(my_obj))
    except TypeError:
        raise TypeError("{} is not JSON serializable".format(my_obj))
