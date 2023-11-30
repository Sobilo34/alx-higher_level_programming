#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    from sys import argv, exit

    count = len(argv)
    if count < 4 or count > 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        nul = [None] * 4
        for index in range(1, count):
            nul[index] = argv[index]

        a = "{} + {} = {}".format(nul[1], nul[3], add(int(nul[1]), int(nul[3])))
        b = "{} + {} = {}".format(nul[1], nul[3], sub(int(nul[1]), int(nul[3])))
        c = "{} + {} = {}".format(nul[1], nul[3], mul(int(nul[1]), int(nul[3])))
        d = "{} + {} = {}".format(nul[1], nul[3], div(int(nul[1]), int(nul[3])))
        
        if nul[2] == '+':
            print(a)
        elif nul[2] == '-':
            print(b)
        elif nul[2] == '*':
            print(c)
        elif nul[2] == '/':
            print(d)
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)

