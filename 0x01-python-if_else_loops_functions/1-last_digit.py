#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    _digit = -number
    _lst = _digit % 10
    _lst = -_lst
else:
    _lst = number % 10
if _lst > 5:
    print(f"Last digit of {number} is {_lst} and is greater than 5")
elif _lst == 0:
    print(f"Last digit of {number} is {_lst} and is 0")
elif _lst < 6 and not 0:
    print(f"Last digit of {number} is {_lst} and is less than 6 and not 0")
