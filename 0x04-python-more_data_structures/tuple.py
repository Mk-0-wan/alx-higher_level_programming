#!/usr/bin/python3
# how to make a function tuple
# passing a function with the same attribute as other defined function you are able to use thier
# defined functionality
a = 23
b = 34
def sub(a, b):
    if a < b:
        return b - a
    else:
        return a - b

def add(a, b):
    return a + b
operation = ['+', '-']
dynamic_func = sub
#dynamic_func = add

res = dynamic_func(int(a), int(b)) # yess you are able to make a function with the same attribute in one line
print("Working with dynamic function")
print("Add value of {:d} {:s} {:d} = {:d}".format(a, operation[1], b, res))
