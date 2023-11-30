#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    count = len(argv)
    if count != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operators = {
        '+': add,
        '-': sub,
        '*': mul,
        '/': div
    }

    if argv[2] in operators:
        dig1 = int(argv[1])
        dig2 = int(argv[3])
        operator_func = operators[argv[2]]
        output = operator_func(dig1, dig2)
        print("{} {} {} = {}".format(dig1, argv[2], dig2, output))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
