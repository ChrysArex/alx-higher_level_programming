#!/usr/bin/python3
"""Define a Rectangle class derived from Base class"""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize the values"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height
        if type(x) is not int:
            raise TypeError("x must be an integer")
        elif x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x
        if type(y) is not int:
            raise TypeError("y must be an integer")
        elif y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y
        super().__init__(id)

    def area(self):
        """Compute the area of an rectangle instance

        Return:
            the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """ Print the rectangle instance with #"""
        offset = ' ' * self.__x
        for i in range(self.__y):
            print()
        for j in range(self.__height):
            print(offset + ('#' * self.__width))

    def update(self, *args, **kwargs):
        """Update the initial data of the Rectangle instance"""
        if args:
            if len(args) == 1:
                super().__init__(args[0])
            elif len(args) == 2:
                super().__init__(args[0])
                self.width = args[1]
            elif len(args) == 3:
                super().__init__(args[0])
                self.width, self.height = args[1:]
            elif len(args) == 4:
                super().__init__(args[0])
                self.width, self.height, self.x = args[1:]
            elif len(args) == 5:
                super().__init__(args[0])
                self.width, self.height, self.x, self.y = args[1:]
        elif kwargs:
            if "id" in kwargs:
                super().__init__(kwargs["id"])
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    @property
    def width(self):
        """Getter for the width

        Return:
            the value of the instance's width
        """
        return self.__width

    @width.setter
    def width(self, new_width):
        """setter for the width

        Args:
            new_width : new value of the width
        """
        if type(new_width) is not int:
            raise TypeError("width must be an integer")
        elif new_width <= 0:
            raise ValueError("width must be > 0")
        self.__width = new_width

    @property
    def height(self):
        """Getter for the height

        Return:
            the value of the instance's height
        """
        return self.__height

    @height.setter
    def height(self, new_height):
        """Setter for the heigth

        Args:
            new_height : new value of the height
        """
        if type(new_height) is not int:
            raise TypeError("height must be an integer")
        elif new_height <= 0:
            raise ValueError("height must be > 0")
        self.__height = new_height

    @property
    def x(self):
        """Getter for the x

        Return:
            the value of the instance's x
        """
        return self.__x

    @x.setter
    def x(self, new_x):
        """Setter for the x

        Args:
            new_x : new value of the x
        """
        if type(new_x) is not int:
            raise TypeError("x must be an integer")
        elif new_x <= 0:
            raise ValueError("x must be > 0")
        self.__x = new_x

    @property
    def y(self):
        """Getter for the y

        Return:
            the value of the instance's y
        """
        return self.__y

    @y.setter
    def y(self, new_y):
        """Setter for the y

        Args:
            new_y : new value of the y
        """
        if type(new_y) is not int:
            raise TypeError("y must be an integer")
        elif new_y <= 0:
            raise ValueError("y must be > 0")
        self.__y = new_y

    def __str__(self):
        """Define a printable value of the Rectangle instance

        Return:
            the string form of the instance
        """
        return "[Rectangle] (" + str(self.id) + ") " + str(self.x) + "/" + \
            str(self.y) + " - " + str(self.width) + "/" + str(self.height)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {
                "id": self.id,
                "width": self.width,
                "height": self.height,
                "x": self.x,
                "y": self.y
                }
