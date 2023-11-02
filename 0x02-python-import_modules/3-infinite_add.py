#!/usr/bin/python3
from sys import argv as av
# first remove the first argument
x = 0
if (len(av) - 1) == 0:
    x = 0

if __name__ == "__main__":
    # start at element[position] 1 to avoid name
    pos = 1
    while pos < len(av):
        # update x with the next argument in line
        x += int(av[pos])
        # move to the next argument
        pos += 1
    print(x)
