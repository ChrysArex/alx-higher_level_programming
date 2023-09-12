#!/usr/bin/python3
import json
"""Define an json file saver
"""


def save_to_json_file(my_obj, filename):
    """useful to write an python Object to a text file

    Args:
        my_obj : the object to write
        filename : the file we want to write it in
    """
    with open(filename, "w", encoding="utf-8") as mf:
        mf.write(json.dumps(my_obj))
