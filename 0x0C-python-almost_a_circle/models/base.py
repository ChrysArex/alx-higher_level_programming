#!/usr/bin/python3
"""Define the base class of all the futur classes"""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            with open("None.json", "w", encoding="utf-8") as mf:
                mf.write("[]")
        else:
            result = []
            if "Rectangle" in str(list_objs[0]):
                name = "Rectangle.json"
            elif "Square" in str(list_objs[0]):
                name = "Square.json"
            for e in list_objs:
                result.append(e.to_dictionary())
            with open(name, "w", encoding="utf-8") as mf:
                mf.write(cls.to_json_string(result))
