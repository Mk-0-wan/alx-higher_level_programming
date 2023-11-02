#!/usr/bin/python3

from sys import argv
from calculator_1 import add, sub, mul, div

# handle the number of argument passed
# failed program should exit with status of 1
# cast all the argument into integers
# output should be like this <a> <operators> <b> = <results>
if (len(argv) - 1) != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>", end='\n')
    exit(1)
# handle the operators
elif argv[2] == "+":
    dynamic_func = add
elif argv[2] == "-":
    dynamic_func = sub
elif argv[2] == "*":
    dynamic_func = mul
elif argv[2] == "/":
    dynamic_func = div
# handle non valid operators
else:
    print("Unknown operator. Available operators: +, -, * and /\n")
    exit(1)

x = dynamic_func(int(argv[1]), int(argv[3]))
print("{:d} {:s} {:d} = {:d}".format(int(argv[1]), argv[2], int(argv[3]), x))
if __name__ != "__main__":
    exit()
