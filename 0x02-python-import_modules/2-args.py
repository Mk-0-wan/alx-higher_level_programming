#!/usr/bin/python3
from sys import argv as av

if __name__ == "__main__":
    index = 1
    x = len(av) - 1

    if (x == 0):
        print(f"{x} arguments.")
    else:
        print("{:d} arguments:".format(x))

    while index < len(av):
        print("{:d}: {:s}".format(index, av[index]))
        index += 1