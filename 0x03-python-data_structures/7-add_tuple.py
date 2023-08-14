#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    val = [0, 0, 0, 0]
    if len(tuple_a) == 1:
        val[0] = tuple_a[0]
    elif len(tuple_a) >= 2:
        val[0], val[1] = tuple_a[0], tuple_a[1]
    if len(tuple_b) == 1:
        val[2] = tuple_b[0]
    elif len(tuple_b) >= 2:
        val[2], val[3] = tuple_b[0], tuple_b[1]
    return (val[0] + val[2], val[1] + val[3])
