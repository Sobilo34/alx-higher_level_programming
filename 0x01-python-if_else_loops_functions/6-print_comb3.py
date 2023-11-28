#!/usr/bin/python3
for count in range(0, 10):
    for iterate in range(0, 10):
        if count != iterate and iterate > count and count < 8:
            print("{}{}, ".format(count, iterate), end='')
        elif count != iterate and iterate > count and count > 7:
            print("{}{}".format(count, iterate))
