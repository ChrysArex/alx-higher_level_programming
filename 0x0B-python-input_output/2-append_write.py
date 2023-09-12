#!/usr/bin/python3
"""Define a text appender
"""


def append_write(filename="", text=""):
    """useful to append a text within a file

    Args:
        filename : name of the file
        text : the text we want to append

    Return:
        The number of char appended
    """
    number = 0
    with open(filename, "a", encoding="utf-8") as mf:
        number = mf.write(text)
    return number
