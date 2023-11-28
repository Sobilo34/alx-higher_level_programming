#!/usr/bin/python3

present_value = 0
count = 90

for number in range(1, 27):
    if number % 2 == 0:
        present_value = count
    else:
        present_value = 123 - number

    count -= 1
    print("{}".format(chr(present_value)), end="")
