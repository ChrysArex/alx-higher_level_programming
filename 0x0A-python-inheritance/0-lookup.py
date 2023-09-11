#!/usr/bin/python3
"""list of attributs

this module define a function that returns the list of available attributes
and methods of an object
"""


def lookup(obj):
    """usefule to find available attributes and methods of an object

    Args:
        obj : the object we want to check the attributes in

    Returns:
         returns the list of available attributes and methods of an object
    """
    return dir(obj)
