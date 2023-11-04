#!/usr/bin/python3
# modifying a list element
# if the indx is out of rang return the original list
# if the indx is less than 0 return the original list
def replace_in_list(my_list, idx, element):
    x = len(my_list)
    if (x == 0):
        exit
    for i in range(0, x):
        if (i == idx):
            my_list[i] = element
            return my_list
        elif idx < 0 or idx > x:
            return my_list
