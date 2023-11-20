#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = int(a) / int(b)
    except (ZeroDivisionError):
        res = None
        print("Inside result: {}".format(res))
        return None
    finally:
        print("Inside result: {}".format(res))
        return res
