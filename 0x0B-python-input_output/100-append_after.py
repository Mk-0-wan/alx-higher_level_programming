#!/usr/bin/python3
"""String searching and manipulation"""


def append_after(filename="", search_string="", new_string=""):
    """Appends a new string at the search matching lines"""
    with open(filename, "r", encoding="utf-8") as fp:
        lst_lines = fp.readlines()

    with open(filename, 'w', encoding="utf-8") as fp:
        for line in lst_lines:
            if search_string in line:
                # append a new one next to it
                line += new_string
            fp.write(line)
