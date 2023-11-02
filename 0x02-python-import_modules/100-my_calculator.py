#!/usr/bin/python3

import sys
import calculator_1

# handle the number of argument passed
# failed program should exit with status of 1
# cast all the argument into integers
# output should be like this <a> <operators> <b> = <results>
if (len(sys.argv) - 1) != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>", end='\n')
    sys.exit(1)
# handle the operators
elif sys.argv[2] == "+":
    res = calculator_1.add(int(sys.argv[1]), int(sys.argv[3]))
    print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {res}")
    sys.exit(0)
elif sys.argv[2] == "+":
    res = calculator_1.add(int(sys.argv[1]), int(sys.argv[3]))
    print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {res}")
    sys.exit(0)
elif sys.argv[2] == "-":
    res = calculator_1.sub(int(sys.argv[1]), int(sys.argv[3]))
    print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {res}")
    sys.exit(0)
elif sys.argv[2] == "*":
    res = calculator_1.mul(int(sys.argv[1]), int(sys.argv[3]))
    print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {res}")
    sys.exit(0)
elif sys.argv[2] == "/":
    res = calculator_1.div(int(sys.argv[1]), int(sys.argv[3]))
    print(f"{sys.argv[1]} {sys.argv[2]} {sys.argv[3]} = {res}")
    sys.exit(0)
# handle non valid operators
else:
    print("Unknown operator. Available operators: +, -, * and /\n")
    sys.exit(1)

if __name__ == "__main__":
    exit()
