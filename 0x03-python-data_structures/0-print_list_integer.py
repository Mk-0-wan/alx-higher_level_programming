#!/usr/bin/python3
# if __name__ != "__main__":
def print_list_integer(my_list=[]):
    x = len(my_list)
    for i in range(0, x):
        print("{:d}".format(int(my_list[i])))
