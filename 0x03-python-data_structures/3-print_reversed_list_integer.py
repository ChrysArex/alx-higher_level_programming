#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    idx = len(my_list) - 1
    for i in my_list:
        print(int('{}'.format(my_list[idx])))
        idx -= 1
