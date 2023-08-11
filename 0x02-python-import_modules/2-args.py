#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    index = 1
    a, b = 's', ':'
    if len(argv) < 2:
        b = '.'
    if len(argv) == 2:
        a = ''
    print("{} argument{}{}".format(len(argv) - 1, a, b))
    if len(argv) >= 2:
        for arg in argv[1:]:
            print("{}: {}".format(index, arg))
            index += 1
