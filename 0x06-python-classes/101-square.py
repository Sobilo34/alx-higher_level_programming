#!/usr/bin/python3

"""
This is to deffine a class square that represent a square"
"""


class Square:
    """This initializes square, determines size and calculates area"""
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    def area(self):
        result = self.__size ** 2
        return result

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) is not tuple or len(value) != 2:
            raise TypeError('position must be a tuple of 2 positive integers')
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError('position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1]:
            raise ValueError('position must be a tuple of 2 positive integers')
        self.__position = value

    def my_print(self):
        if self.size == 0:
            print('')
            return
        for i in range(self.__position[1]):
            print('')
        for i in range(self.__size):
            print("{}{}".format(' ' * self.__position[0], '#' * self.__size))

    def __str__(self):
        if self.__size == 0:
            return ''
        new_lines = '\n' * self.position[1]
        spaces = ' ' * self.position[0]
        hashes = '#' * self.size
        return new_lines + '\n'.join(spaces + hashes for e in range(self.size))
