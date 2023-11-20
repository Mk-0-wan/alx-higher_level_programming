#!/usr/bin/python3
def safe_print_integer(value):
    try:
        if (value.__class__ == int):
            print("{:d}".format(int(value)))
            return True
    except (ValueError):
        return (False)
