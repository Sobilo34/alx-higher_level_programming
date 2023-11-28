#!/usr/bin/python3

current_value = 0
countdown = 90

for num in range(1, 27):
    if num % 2 == 0:
        current_value = countdown
    else:
        current_value = 123 - num

    countdown -= 1
    print("{}".format(chr(current_value)), end="")
