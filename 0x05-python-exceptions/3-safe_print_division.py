#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = int(a) / int(b)
        return res
    except (ZeroDivisionError):
        res = None
    finally:
        print("Inside result: {}".format(res))
