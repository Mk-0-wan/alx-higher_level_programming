#!/usr/bin/python3
"""Matrix Operation in python3"""


def matrix_divided(matrix, div):
    """Python function that does some division to
    each element in the matrix

    Args:
        matrix (list of lists): a list of lists containing the values
        div (int or float): value to divide the matrix element with

    Return:
        a new matrix with the new value after division by div
    """

    if not isinstance(div, (float, int)):
        raise TypeError("div must be number")
        return matrix
    elif div == 0:
        raise ZeroDivisionError("division by zero")
        return matrix

    row_len = -1
    new_matrix = []

    for row in matrix:
        if (row_len != len(row) and row_len != -1):
            raise TypeError("Each row of the matrix must have the same size")
            return matrix
        for items in row:
            if not isinstance(items, (float, int)):
                raise TypeError("matrix must be a matrix " +
                                "(list of lists) of integers/floats")
                return matrix
            else:
                new_matrix.append(round(items / div, 2))
        row_len = len(row)

    return new_matrix
