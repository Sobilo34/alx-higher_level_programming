#!/usr/bin/python3
for count in range(0, 10):
    for iterate in range(count + 1, 10):
        if count < 8:
            print("{}{}, ".format(count, iterate), end='')
        elif count > 7:
            print("{}{}".format(count, iterate))
