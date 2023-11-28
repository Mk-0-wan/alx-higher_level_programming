#!/usr/bin/python3
"""Lazy matrix multiplication"""


def lazy_matrix_mul(m_a, m_b):
    """Lazy multiplication with numpy

    Args:
        m_a: matrix a
        m_b: matrix b
    Return:
        multiplication of a and b
    """
    import numpy

    ret = numpy.dot(m_a, m_b)

    return ret
