#!/usr/bin/python3
"""Define the base class of all the futur classes"""


class Base():
    """Class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialized the values of id

        Args:
            id : identifier of the base instance
        """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
