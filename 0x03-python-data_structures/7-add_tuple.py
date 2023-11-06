#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_b) == 1:
        tuple_3 = (tuple_a[0]+tuple_b[0], tuple_a[1]+0)
    elif len(tuple_b) == 0:
        return tuple_a
    elif len(tuple_b) > 1:
        tuple_3 = (tuple_a[0]+tuple_b[0], tuple_a[1]+tuple_b[1])
    return tuple_3
