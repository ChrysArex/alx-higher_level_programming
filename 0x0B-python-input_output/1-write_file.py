#!/usr/bin/python3
"""Define a function to write within a file
"""


def write_file(filename="", text=""):
    """useful to write within a file

    Args:
        filename : name of the file
        text : the text we want to insert

    Return:
        the number of char written
    """
    number = 0
    with open(filename, "w", encoding="utf-8") as mf:
        number = mf.write(text)
    return number
