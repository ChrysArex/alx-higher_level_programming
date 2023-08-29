#!/usr/bin/python3
"""Square class, private and public attribute, setter and getter

this module define a Square class that have an integer attribute size
It also raise some exceptions to handle the size type. It contains
additionals public instance methode, getter and setter
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

    def size(self):
        """getter for the size of the square

        Return:
            size of the square
        """
        return self.__size

    def size(self, value):
        """change the size of the square

        Args:
            value: the new size of the square
        """
        try:
            value + 1
        except TypeError:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
