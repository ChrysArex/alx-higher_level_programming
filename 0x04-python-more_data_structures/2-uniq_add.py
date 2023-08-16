#!/usr/bin/python3
def uniq_add(my_list=[]):
    total = 0
    for e in set(my_list):
        total += e
    return total
