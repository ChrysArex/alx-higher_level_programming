#! /usr/bin/python

def fizzbuzz():
    for i in range(1, 101):
        value = i
        value_1, value_2 = "", ""
        if i % 3 == 0:
            value_1 = "Fizz"
        if i % 5 == 0:
            value_2 = "Buzz"
        if value_1 or value_2:
            print(value_1 + value_2, end=" ")
        else:
            print(value, end=" ")
