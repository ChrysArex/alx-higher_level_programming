#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nbr = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
        except (ValueError, TypeError):
            continue
        else:
            nbr += 1
    print()
    return nbr
