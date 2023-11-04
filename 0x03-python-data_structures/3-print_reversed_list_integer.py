#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list = my_list[::-1]
    element, x = 0, 0
    while x < len(my_list)-1:
        print("{:d}".format(int(my_list[element])))
        element, x = element+1, x+1
