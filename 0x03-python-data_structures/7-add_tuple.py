#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    len_a = len(tuple_a)
    len_b = len(tuple_b)
    tuple_c = ()
    for idx in range(2):
        pos_1 = tuple_a[idx] if idx < len_a else 0
        pos_2 = tuple_b[idx] if idx < len_b else 0
        # at the first iteration make a new tuple
        if (idx == 0):
            tuple_c = pos_1 + pos_2
        else:
            # add new items to the tuple
            tuple_c = tuple_c, pos_1 + pos_2
    return tuple_c
