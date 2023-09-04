#!/usr/bin/python3
"""This module define the Rectangle class

This version add two private instance attributes with they setter and getter
"""


class Rectangle:
    """Rectangle with his height and width

    Attributes:
        number_of_instances (int): number of Rectangle object created
        print_symbol (:obj:`str`, optional): used as symbol
        for string representation
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize the width and the height of the rectangle
        """
        type(self).number_of_instances += 1
        self.__width = width
        self.__height = height
        self.__a = None

    def __str__(self):
        """useful to print the rectangle

        Return:
            the rectangle with the character #
        """
        self.__a = ""
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            try:
                for i in range(1, self.__height):
                    self.__a += str(self.print_symbol)*self.__width + '\n'
                self.__a += str(self.print_symbol)*self.__width
            except AttributeError:
                for i in range(1, self.__height):
                    self.__a += str(type(self).print_symbol)*self.__width +\
                            '\n'
                self.__a += str(type(self).print_symbol)*self.__width
            return self.__a

    def __repr__(self):
        """useful to recreate this instance of Rectangle

        Return:
            A string representing this instance of Rectangle
        """
        return "Rectangle(" + str(self.__width) + ", "\
            + str(self.__height) + ")"

    def __del__(self):
        """print a message when an instance is deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    @classmethod
    def symbol(cls):
        """get th symbole to use

        Return:
            the symbole to use when printing the Rectangle
        """
        return cls.print_symbol

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """determine the bigest rectangle

        Args:
            rect_1 : first rectangle to compare
            rect_2 : second rectangle to compare
        Return:
            The bigest rectangle
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        elif type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        else:
            if rect_1.area() >= rect_2.area():
                return rect_1
            else:
                return rect_2

    @classmethod
    def square(cls, size=0):
        """create a square

        Return:
            returns a new Rectangle instance with width == height == size
        """
        return cls(size, size)
