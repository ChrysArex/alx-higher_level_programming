#!/usr/bin/python3
"""Square class, private and public attribute, setter and getter

this module define a Square class that have an integer attribute size
It also raise some exceptions to handle the size type. It contains
additionals public instance methode, getter and setter
"""


class Square:
    """Square class with private attribute
    """

    def __init__(self, size=0, position=(0, 0)):
        """create a private instance attribute

        Args:
            size (int): size of the square
        """
        self.__size = size
        self.__position = position

    def area(self):
        """Compute the area of the square

        Return:
            current square area
        """
        return self.__size**2

    @property
    def size(self):
        """getter for the size of the square

        Return:
            size of the square
        """
        return self.__size

    @size.setter
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

    def my_print(self):
        """ prints in stdout the square with the character #
        """
        tmp = self.__position[1]
        if self.__size == 0:
            print()
        else:
            while (tmp != 0):
                print()
                tmp -= 1
            for i in range(0, self.__size):
                print(" "*self.__position[0], end="")
                print("#"*self.__size)

    @property
    def position(self):
        """getter to retrieve the position

        Return:
            position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """set the value of the position

        Args:
            value (tuple): coordonates of the square
        """
        if type(value) is tuple:
            try:
                if value[0] < 0 or value[1] < 0:
                    raise TypeError("position must be a tuple of\
                            2 positive integers")
                self.__position = value
            except (ValueError, TypeError):
                raise TypeError("position must be a tuple of\
                        2 positive integers")
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
