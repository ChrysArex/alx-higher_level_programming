#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    index = 1
    if len(argv) < 2:
        a, b = '', '.'
    else:
        a, b = 's', ':'
    print(f"{len(argv) - 1} argument{a}{b}")
    if a:
        for arg in argv[1:]:
            print(f"{index}: {arg}")
            index += 1
