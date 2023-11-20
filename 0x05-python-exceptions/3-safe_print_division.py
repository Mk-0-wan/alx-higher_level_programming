#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        res = int(a) / int(b)
        return res
    except (ZeroDivisionError):
        res = None
    finally:
        print("Inside result: {}".format(res))

a = 12
b = 2
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))

a = 12
b = 0
result = safe_print_division(a, b)
print("{:d} / {:d} = {}".format(a, b, result))
