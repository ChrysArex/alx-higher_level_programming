#!/usr/bin/python3
import sys as s


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as err:
        s.stderr.write("Exception: {}\n".format(err))
        return False
    else:
        return True
