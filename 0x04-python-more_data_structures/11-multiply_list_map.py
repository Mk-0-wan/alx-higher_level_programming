#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    return list(map(int.__mul__, my_list, [number] * len(my_list)))
