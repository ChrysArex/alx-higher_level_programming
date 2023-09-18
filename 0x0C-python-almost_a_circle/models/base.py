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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        new = cls(1, 1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""
        if "Rectangle" in str(cls):
            filename = "Rectangle.json"
        elif "Square" in str(cls):
            filename = "Square.json"
        try:
            mf = open(filename, "r", encoding="utf-8")
        except FileNotFoundError:
            return []
        old_instances = cls.from_json_string(mf.read())
        new_instances = []
        for e in old_instances:
            new_instances.append(cls.create(**e))
        mf.close()
        return new_instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""
        if list_objs is None:
            with open("None.csv", "w", encoding="utf-8") as mf:
                mf.write("[]")
        else:
            result = []
            if "Rectangle" in str(list_objs[0]):
                name = "Rectangle.csv"
                with open(name, "w", encoding="utf-8") as mf:
                    for e in list_objs:
                        mf.write("{},{},{},{},{}\n".format(
                            e.id, e.width, e.height, e.x, e.y
                            ))
            elif "Square" in str(list_objs[0]):
                name = "Square.csv"
                with open(name, "w", encoding="utf-8") as mf:
                    for e in list_objs:
                        mf.write("{},{},{},{}\n".format(
                            e.id, e.size, e.x, e.y
                            ))

    @classmethod
    def load_from_file_csv(cls):
        """deserialize csv file"""
        if "Square" in str(cls):
            filename = "Square.csv"
            try:
                mf = open(filename, "r", encoding="utf-8")
            except FileNotFoundError:
                return []
            new_instances = []
            for e in mf.readlines():
                token = e.split(',')
                new_instances.append(cls(
                    int(token[1]), int(token[2]),
                    int(token[3]), int(token[0])
                    ))
            mf.close()
            return new_instances
        elif "Rectangle" in str(cls):
            filename = "Rectangle.csv"
            try:
                mf = open(filename, "r", encoding="utf-8")
            except FileNotFoundError:
                return []
            new_instances = []
            for e in mf.readlines():
                token = e.split(',')
                new_instances.append(cls(
                    int(token[1]), int(token[2]),
                    int(token[3]), int(token[4]),
                    int(token[0])
                    ))
            mf.close()
            return new_instances
