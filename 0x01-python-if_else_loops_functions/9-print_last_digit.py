#! /usr/bin/python3

def print_last_digit(number):
    sign = 1
    p_number = number
    if number < 0:
        sign = -1
        p_number = number * -1
    print(p_number % 10, end="")
    return (p_number % 10)
