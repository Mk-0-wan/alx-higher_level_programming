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
    res = add(int(sys.argv[1]), int(sys.argv[3]))
    print(f"{argv[1]} {argv[2]} {argv[3]} = {res}")
    exit(0)
elif argv[2] == "-":
    res = sub(int(argv[1]), int(argv[3]))
    print(f"{argv[1]} {argv[2]} {argv[3]} = {res}")
    exit(0)
elif argv[2] == "*":
    res = mul(int(sys.argv[1]), int(sys.argv[3]))
    print(f"{argv[1]} {argv[2]} {argv[3]} = {res}")
    exit(0)
elif argv[2] == "/":
    res = div(int(sys.argv[1]), int(sys.argv[3]))
    print(f"{argv[1]} {argv[2]} {argv[3]} = {res}")
    exit(0)
# handle non valid operators
else:
    print("Unknown operator. Available operators: +, -, * and /\n")
    exit(1)

if __name__ == "__main__":
    exit()
