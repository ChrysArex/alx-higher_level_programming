#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv, exit
    from calculator_1 import add, sub, mul, div
    print(argv)
    if len(argv) != 4:
        print(argv)
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    if argv[2] not in ['+', '-', '*', '/']:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
    if argv[2] == '+':
        result = add(int(argv[1]), int(argv[3]))
    if argv[2] == '-':
        result = sub(int(argv[1]), int(argv[3]))
    if argv[2] == '*':
        result = mul(int(argv[1]), int(argv[3]))
    if argv[2] == '/':
        result = div(int(argv[1]), int(argv[3]))
    print("{} {} {} = {}".format(argv[1], argv[2], argv[3], result))
