#!/usr/bin/python3
"""Define a custom int class
"""


class MyInt(int):
    """rebel class int
    """
    def __init__(self, val):
        """initialise the value of int
        """
        self.__val = val

    def __eq__(self, comp):
        """inverse the equal value
        """
        return (not (self.__val == comp))

    def __ne__(self, comp):
        """inverse the non-equal value
        """
        return (not (self.__val != comp))
