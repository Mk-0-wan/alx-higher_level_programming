#!/usr/bin/python3
from sm_math_operation import add, sub


def magic_calculation(a, b):
    if (a < b):
        c = add(a, b)
        for i in range(4, 6):
            c = add(i, c)
        return (c)
    else:
        return (sub(a, b))
