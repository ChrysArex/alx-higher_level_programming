#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    total_weight = 0
    average = 0
    for e in my_list:
        total_weight += e[1]
    for i in list(map(lambda x: x[0] * x[1], my_list)):
        average += i
    return average/total_weight
