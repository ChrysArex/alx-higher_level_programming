#!/usr/bin/python3
"""Define a file reader function
"""


def read_file(filename=""):
    """usefule to read a txt file

    Arg:
        filename : name of the file we want to open
    """
    with open(filename, encoding="utf-8") as mf:
        for line in mf.readlines():
            print(line, end="")
