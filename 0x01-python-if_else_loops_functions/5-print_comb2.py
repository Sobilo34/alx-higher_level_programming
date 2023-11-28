#!/usr/bin/python3
for count in range(0, 100):
    if count == 99:
        print("{:02d}".format(count))
    elif count < 99:
        print("{:02d}, ".format(count), end="")
