#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        if len(i) <= 0:
            continue
        for j in i[:len(i) - 1]:
            print(int("{:n}".format(j)), end="")
            print(' ', end="")
        print(int("{:n}\n".format(i[(len(i)-1)])))
