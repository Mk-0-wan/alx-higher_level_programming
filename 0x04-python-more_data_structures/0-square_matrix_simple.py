#!/usr/bin/python3
def sq(int):
    return int**2


def square_matrix_simple(matrix=[]):
    return [[sq(col) for col in row] for row in matrix]
