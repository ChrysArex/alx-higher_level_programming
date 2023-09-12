#!/usr/bin/python3
import json
"""Define an python object getter
"""


def from_json_string(my_str):
    """useful to get python object from str

    Args:
        my_str : the string we want to convert

    Return:
        the python object
    """
    return json.loads(my_str)
