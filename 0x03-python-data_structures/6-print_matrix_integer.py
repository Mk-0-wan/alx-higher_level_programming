#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == []:
        print()
    for row in matrix:
        for i, col in enumerate(row):
            print("{:d}".format(int(col)), end=(' ', '\n')[i == len(row) - 1])
