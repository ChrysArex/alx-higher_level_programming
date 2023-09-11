#!/usr/bin/python3
"""redefine the BaseGeometry class
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
            Value :the value herself
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
