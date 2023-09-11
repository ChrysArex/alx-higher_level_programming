#!/usr/bin/python3
"""Define a function to check the class
"""


def inherits_from(obj, a_class):
    """usful to determine a class or inherite class

    Args:
        obj: the object we want to check
        a_class: the class
    """
    if isinstance(obj, a_class):
        if type(obj) is a_class:
            return False
        else:
            return True
    else:
        return False
