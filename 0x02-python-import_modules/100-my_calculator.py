#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    count = len(argv)
    if count < 4 or count > 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        n = [None] * 4
        for index in range(1, count):
            i[index] = argv[index]

        a = "{} + {} = {}".format(i[1], i[3], add(int(i[1]), int(i[3])))
        b = "{} - {} = {}".format(i[1], i[3], sub(int(i[1]), int(i[3])))
        c = "{} * {} = {}".format(i[1], i[3], mul(int(i[1]), int(i[3])))
        d = "{} / {} = {}".format(i[1], i[3], div(int(i[1]), int(i[3])))

        if i[2] == '+':
            print(a)
        elif i[2] == '-':
            print(b)
        elif i[2] == '*':
            print(c)
        elif i[2] == '/':
            print(d)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
