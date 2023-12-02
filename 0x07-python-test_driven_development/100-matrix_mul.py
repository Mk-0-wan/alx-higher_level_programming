#!/usr/bin/python3
"""Matrix Multiplication"""


def matrix_mul(m_a, m_b):
    """Matrix multiplication with a python function

    Args:
        m_a (list): matrix a
        m_b (list): matrix b to multiply with a
    Return:
        a new matrix from the multiplication of a and b
    """

    # checking for lists in matrix
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # checking for list of lists in matrix
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # checking for empty matrices
    if m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # checking for element types
    if not all(isinstance(items, (int, float))
               for row in m_a for items in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(items, (int, float))
               for row in m_b for items in row):
        raise TypeError("m_b should contain only integers or floats")

    # get the length of the first list in the matrices
    # checking for all perfect matrices
    for row in m_a:
        if len(row) != len(m_a[0]):
            raise TypeError("each row of m_a must be of the same size")

    for row in m_b:
        if len(row) != len(m_b[0]):
            raise TypeError("each row of m_b must be of the same size")

    # checking for compatibility during multiplication
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # the zip function iterates over several iterables in parallel order
    # while returning a tuples
    # a = [1, 2, 3]
    # b = ['sugar', 'spice', 'salt']
    # for item in zip(a, b):
    #       print(item)
    # ----output-----
    # (1, 'sugar')
    # (2, 'spice')
    # (3, 'salt')
    # dot product
    # [ a, b ][ x , i ]  = [ ax + by , ai + bj ] 1row * 1col
    # [ c, d ][ y , j ]  = [ cx + dy , ci + dj ] 2row * 2col
    # matrix dot product calc with python list comprehension
    m_c = [
            [
                # same as [ ax + by ]
                sum(a_row * b_col for a_row, b_col in zip(m_a_row, m_b_col))
                # move to the next col
                for m_b_col in zip(*m_b)
             ]
            # move to the next row
            for m_a_row in m_a
            ]
    return m_c
