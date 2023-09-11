#!/usr/bin/python3
"""Define the Rectangle class that inherits from the BaseGeometry class
"""


class BaseGeometry():
    """An improved version of BaseGeometry class
    """
    def area(self):
        """Raise an Exception
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate value

        Args:
            name : name of the value
            Value : the value herself
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class derived from the BaseGeometry class
    """
    def __init__(self, width, height):
        """initialize the width and the height

        Args:
            width : the width of the rectangle
            height : the height of the rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
