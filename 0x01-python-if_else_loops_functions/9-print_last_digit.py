#!/usr/bin/python3

def print_last_digit(number):
    if (number < 0):
        number *= -1
    ret = number % 10
    print(ret, end='')
    return (ret)
