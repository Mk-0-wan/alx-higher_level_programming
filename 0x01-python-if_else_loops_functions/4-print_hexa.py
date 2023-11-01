#!/usr/bin/python3

for i in range(0, 99):
    print("{:d} = 0x{:x}".format(i, i) if i < 99 else '\n')
