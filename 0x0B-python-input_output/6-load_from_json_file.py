#!/usr/bin/python3
import json
"""Define a python objet getter (from file)
"""


def load_from_json_file(filename):
    """usefule to load python obj from json file

    Args:
        filename : the file we load the obj from

    Return:
        the python obj
    """
    with open(filename, encoding="utf-8") as mf:
        return json.loads(mf.read())
