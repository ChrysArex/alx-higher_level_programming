#!/usr/bin/python3
"""Define the Square class derived from the Rectangle one"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Class Square"""
    def __init__(self, size, x=0, y=0, id=None):
        """Initialize the attributes"""
        super().__init__(size, size, x, y, id)

    def update(self, *args, **kwargs):
        """Update the value of the attributs"""
        if args:
            if len(args) == 1:
                super().__init__(self.size, self.size, self.x, self.y, args[0])
            elif len(args) == 2:
                super().__init__(self.size, self.size, self.x, self.y, args[0])
                self.width = args[1]
                self.height = args[1]
            elif len(args) == 3:
                super().__init__(self.size, self.size, self.x, self.y, args[0])
                self.width, self.height, self.x = args[1], args[1], args[2]
            elif len(args) == 4:
                super().__init__(self.size, self.size, self.x, self.y, args[0])
                self.width, self.height = args[1], args[1]
                self.x, self.y = args[2:]
        elif kwargs:
            if "id" in kwargs:
                switch = kwargs["id"]
                super().__init__(self.size, self.size, self.x, self.y, switch)
            if "size" in kwargs:
                self.width = kwargs["size"]
                self.height = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def __str__(self):
        """String representation of the square instance"""
        return "[Square] (" + str(self.id) + ") " + str(self.x) + "/" \
            + str(self.y) + " - " + str(self.width)

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        return {
                "id": self.id,
                "size": self.width,
                "x": self.x,
                "y": self.y
                }

    @property
    def size(self):
        """getter for the size"""
        return self.width

    @size.setter
    def size(self, new_size):
        """setter for the size"""
        self.width = new_size
        self.height = new_size
