#!/usr/bin/python3

def uppercase(str):
    index = 0
    for i in str:
        asc_value = ord(i)
        if ord(i) >= 97 and ord(i) <= 122:
            asc_value = ord(i) - 32
        value = chr(asc_value)
        if (index + 1 != len(str)):
            print("{}".format(value), end="")
        elif (index + 1 == len(str)):
            print("{}".format(value))
        index += 1
