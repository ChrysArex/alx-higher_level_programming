#!/usr/bin/python3
"""module with Square class with private and public attribute

this module define a Square class that have an integer attribute size
It also raise some exceptions to handle the size type. It contains
an additional public instance methode
"""


class Square:
    """Square class with private attribute
    """

    def __init__(self, size=0):
        """create a private instance attribute

        Args:
            size (int): size of the Square
        """
        try:
            size + 1
        except TypeError:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Compute the area of the square

        Return:
            current square area
        """
        return self.__size**2
