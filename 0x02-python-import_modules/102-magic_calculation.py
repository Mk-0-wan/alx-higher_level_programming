#!/usr/bin/python3

def magic_calculation(a, b):
    from sm_math_operation import add, sub
    if (a < b):
        c = add(a, b)
        for i in range(4, 6):
            c = add(i, c)
            return (c)
    else:
        return (sub(a, b))
