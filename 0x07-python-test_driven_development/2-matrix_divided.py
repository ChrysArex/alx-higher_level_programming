#!/usr/bin/python3
"""Def of a matrix divider

This module define a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """Useful to divide all elmts of a matrix

    Args:
        matrix : the matrix to divide
        div : the element to divide by

    Return:
        new matrix with the divided elements
    """
    idx = 0
    new = []
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    elif type(matrix) is not list or len(matrix) == 0:
        raise TypeError("matrix must be a matrix (list of lists) "\
                "of integers/floats")
    else:
        for e in matrix:
            if type(e) is not list or len(e) == 0:
                raise TypeError("matrix must be a matrix (list of lists) "\
                        "of integers/floats")
            else:
                for i in e:
                    if type(i) not in [int, float]:
                        raise TypeError("matrix must be a matrix "\
                                "(list of lists) of integers/floats")
                if idx >= 1 and len(matrix[idx]) != len(matrix[idx - 1]):
                    raise TypeError("Each row of the matrix "\
                            "must have the same size")
                new.append(list(map(lambda x: round(x/div, 2), e)))
            idx += 1
        return new
