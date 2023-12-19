#!/usr/bin/python3

"""
class Square that defines a square by: (based on 4-square.py
"""

class Square:
    """To instantiate variable and raise errors for exeptions"""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size != 0:
            for _ in range(self.__size):
                print("#" * self.__size)
        else:
            print()

if __name__ == "__main__":
    square1 = Square(5)
    print("Area of square1:", square1.area())
    square1.my_print()

    square2 = Square()
    print("Area of square2:", square2.area())
    square2.my_print()
