#!/usr/bin/python3
def uppercase(str):
    for count in str:
        if 'a' <= count <= 'z':
            count = chr(ord(count) - 32)
        else:
            count = count
        print("{}".format(count), end="")
    print("")
