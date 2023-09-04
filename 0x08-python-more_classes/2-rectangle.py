#!/usr/bin/python3
"""This module define the Rectangle class

This version add two private instance attributes with they setter and getter
"""


class Rectangle:
    """Rectangle with his height and width
    """

    def __init__(self, width=0, height=0):
        """Initialize the width and the height of the rectangle
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """width: the width of the rectangle

        Return:
            The width of the rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the width

        Args:
            value: new value
        """
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height: the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the height"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """compute the area of the rectangle

        Return:
            The area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """compute the perimeter

        Return:
            The perimeter of the rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (self.__width + self.__height) * 2
