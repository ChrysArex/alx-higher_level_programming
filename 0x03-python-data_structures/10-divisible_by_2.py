#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    is_mult = [False for i in range(len(my_list))]
    idx = 0
    for i in my_list:
        if i % 2 == 0:
            is_mult[idx] = True
        idx += 1
    return is_mult
