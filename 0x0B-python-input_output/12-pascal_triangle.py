#!/usr/bin/python3
"""Define a function that create a Pascal's triangle
"""


def pascal_triangle(n):
    """Create a the Pascal’s triangle of n

    Args:
        n : the number

    Return:
        returns a list of lists of integers representing the Pascal’s
        triangle of n
    """
    result = [[1], [1, 1]]
    if n <= 0:
        return []
    elif n == 1:
        return [[1]]
    elif n == 2:
        return [[1], [1, 1]]
    while len(result) < n:
        size = len(result[len(result) - 1]) - 1
        row = result[len(result) - 1]
        add = [1]
        for e in range(0, size):
            add.append(row[e] + row[e + 1])
        add.append(1)
        result.append(add)
    return result
