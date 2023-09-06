#!/usr/bin/python3
"""Usefule to make addition

this module define a function that make addition
"""


def add_integer(a, b=98):
    """add two integers

    Args:
        a (int): first int
        b (int): second int

    Return:
        The sum of the two args

    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    elif type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    try:
        return a + b
    except TypeError:
        print("Please provide at least a")
