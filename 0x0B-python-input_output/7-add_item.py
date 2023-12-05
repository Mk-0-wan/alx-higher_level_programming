#!/usr/bin/python3
"""Reading and Writing to a json file"""
import json
import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def read_write_to_json():
    """simple python function that writes to a file"""
    try:
        lst = load_from_json_file("add_item.json")
    except Exception:
        lst = []

    lst.extend([sys.argv[i] for i in range(len(sys.argv)) if i != 0])

    save_to_json_file(lst, "add_item.json")


if __name__ == "__main__":
    read_write_to_json()
