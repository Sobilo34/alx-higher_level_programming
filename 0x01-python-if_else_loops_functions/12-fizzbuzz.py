#!/usr/bin/python3
def fizzbuzz():
    for counting in range(1, 101):
        if counting % 15 == 0:
            print("FizzBuzz ", end="")
        elif (counting % 3) == 0:
            print("Fizz ", end='')
        elif (counting % 5) == 0:
            print("Buzz ", end='')
        else:
            print("{} ".format(counting), end="")
