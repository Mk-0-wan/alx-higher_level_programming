#!/usr/bin/python3
# how to retrive an element from a list with a given index
# if the index is out of range return none
# if the index is -1 return none
def element_at(my_list, idx):
    x = len(my_list)
    for i in range(0, x+1):
        if (i == idx):
            return my_list[i]
        elif idx < 0 or idx > x:
            return None
