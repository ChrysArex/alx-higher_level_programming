#!/usr/bin/python3
import json
"""Define a JSON serializer
"""


def to_json_string(my_obj):
    """useful to get the JSON representation of python object

    Args:
        my_obj : the object

    Return:
        the JSON representation of my_obj
    """
    return json.dumps(my_obj, sort_keys=True)
