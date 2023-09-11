#!/usr/bin/python3
"""Define class checker
define a class that check wether an given object in an instance of a given
class
"""


def is_same_class(obj, a_class):
    """useful to know an instance of an a_class

    Args:
       obj : the obj we want to check
       a_class: the class
    """
    return type(obj) is a_class
