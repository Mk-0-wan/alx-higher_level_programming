#!/usr/bin/python3
import dis

def magic_function(a, b):
    return 98 + (a ** b)

print(dis.dis(magic_function))
