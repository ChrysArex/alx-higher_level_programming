#!/usr/bin/python3
"""Define a key:value attribut getter
"""


def class_to_json(obj):
    """useful to key:value instance attribut

    Args:
        obj : the object we want the attributs from
    """
    return vars(obj)
