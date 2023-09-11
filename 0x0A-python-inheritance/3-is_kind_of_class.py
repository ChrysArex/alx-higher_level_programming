#!/usr/bin/python3
"""Define a function to check the class
"""


def is_kind_of_class(obj, a_class):
    """usful to determine a class or inherite class

    Args:
        obj: the object we want to check
        a_class: the class
    """
    return isinstance(obj, a_class)
