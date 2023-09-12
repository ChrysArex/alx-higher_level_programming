#!/usr/bin/python3
"""Define a class student
"""


class Student():
    """Class student
    """

    def __init__(self, first_name, last_name, age):
        """Initialize instance variables
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """useful to retrive dictionnary of instance variable

        Args:
            attrs : the attribut list

        Return:
            The dictionnary
        """
        wanted_vals = {}
        if not attrs:
            return vars(self)
        else:
            for e in attrs:
                if e in vars(self):
                    wanted_vals[e] = vars(self)[e]
            return wanted_vals
