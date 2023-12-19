#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        self.size = size

    def area(self):
        return self.size ** 2

if __name__ == "__main__":
    square1 = Square(5)
    print("Area of square1:", square1.area())

    square2 = Square()
    print("Area of square2:", square2.area())

