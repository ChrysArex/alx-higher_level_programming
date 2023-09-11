#!/usr/bin/python3
"""Define class checker
"""


def is_same_class(obj, a_class):
    """useful to know an instance of an a_class

    Args:
       obj : the obj we want to check
       a_class: the class
    """
    if a_class is object:
        return False
    else:
        return isinstance(obj, a_class)
