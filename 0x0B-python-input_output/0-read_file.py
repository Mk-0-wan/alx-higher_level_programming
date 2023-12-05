#!/usr/bin/python3
"""Reading from a file"""


def read_file(filename=""):
    """function that reads all the contents of a file

   Args:
        filename (str):name of the file to write to
    """
    with open(filename, encoding="utf-8") as fp:
        print(fp.read().strip())
