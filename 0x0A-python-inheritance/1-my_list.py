#!/usr/bin/python3
"""define the MyList class

Define a new class that inherits from list and implemant a new
instance method: def print_sorted(self): that prints the list, but sorted
(ascending sort)

"""


class MyList(list):
    """subclass of list
    """
    def print_sorted(self):
        """useful to print sorted version on this object
        """
        print(sorted(self))
