#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestBase(unittest.TestCase):

    def id_increment_test(self):
        """
        This is the unnitest that test if an id is
        incremented at every new instance of base
        """
        instance_1 = Base()
        instance_2 = Base()
        self.assertEqual(instance_1.id, 1)  # Test if id is incremented by 1
        self.assertEqual(instance_2.id, 2)  # Tests if id is incremented by another 1

    def id_correctness_test(self):
        """
        This is the unittest that test that the
        correcteness of an id when passed as an argument to Base
        """
        base_instance = Base(100)
        self.assertEqual(base_instance.id, 100)

    def mixed_instance_test(self):
        """
        This is to test if id is incremented for different classes
        """
        base_instance = Base()
        rectg_instance = Rectangle(5, 10)
        square_instance = square(3)
        self.assertEqual(base_instance.id, 1)  # check increment of base, no argumnet for base
        self.assertEqual(rectg_instance.id, 2)  # check increment for rectangle
        self.assertEqual(square_instance.id, 3)  # check increment of square

class TestRectangle(unittest.TestCase):
    def rect_attributes_test(self):
        """
        Unittest that test the attribute of the rectangle
        """
        rectg_instance = Rectangle(5, 10)
        self.assertEqual(rectg_instance.width, 5)
        self.assertEqual(rectg_instance.height, 10)

        # Add more test cases for Rectangle class

class TestSquare(unittest.TestCase):

    def square_attributes_test(self):
        """
        Test specific attributes and behaviors of Square class
        """
        square_instance = Square(3)
        self.assertEqual(square_instance.size, 3)

        # Add more test cases for Square class

if __name__ == '__main__':
    unittest.main()
