#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = 1
p_number = number
if number < 0:
    sign = -1
    p_number = number * -1
if (p_number % 10)*sign > 5:
    print("Last digit of {0} is {1} and is greater than 5".format(
        number, (p_number % 10)*sign))
elif (p_number % 10)*sign == 0:
    print("Last digit of {0} is {1} and is 0".format(
        number, (p_number % 10)*sign))
elif ((p_number % 10)*sign < 6 and
        (p_number % 10)*sign != 0):
    print("Last digit of {0} is {1} and is less than 6 and not 0".format(
        number, (p_number % 10)*sign))
