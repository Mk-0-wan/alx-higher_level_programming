#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        if (b > 0):
            res = int(a) / int(b)
        else:
            raise ZeroDivisionError
    except (ZeroDivisionError):
        res = None
        print("Inside result: {}".format(res))
        return None
    finally:
        print("Inside result: {}".format(res))
        return res
