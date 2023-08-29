#!/usr/bin/python3
"""Enhanced Square class

This module define a class Square that take a private size argument.
"""


class Square:
    """One attribute class Square
    """

    def __init__(self, size):
        """initiate the size of the square

        Args:
            size (int): size of the square
        """
        self.__size = size
