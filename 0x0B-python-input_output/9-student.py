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

    def to_json(self):
        """useful to retrive dictionnary of instance variable

        Return:
            The dictionnary
        """
        return vars(self)
