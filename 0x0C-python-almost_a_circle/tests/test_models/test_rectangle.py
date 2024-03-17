#!/usr/bin/python3

import unittest
from models.rectangle import Rectangle
from unittest.mock import patch
import io

class TestRectangle(unittest.TestCase):

    def test_constructor(self):
        rectangle = Rectangle(4, 5, 1, 2, 10)
        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 5)
        self.assertEqual(rectangle.x, 1)
        self.assertEqual(rectangle.y, 2)
        self.assertEqual(rectangle.id, 10)

    def test_area(self):
        rectangle = Rectangle(4, 5)
        self.assertEqual(rectangle.area(), 20)

    def test_display(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            r = Rectangle(3, 2)
            r.display()
            expected_output = "###\n###\n"
            self.assertEqual(mock_stdout.getvalue().strip(), expected_output.strip())

    def test_str(self):
        rectangle = Rectangle(4, 5, 1, 2, 10)
        expected_str = "[Rectangle] (10) 1/2 - 4/5"
        self.assertEqual(str(rectangle), expected_str)

    def test_update_args(self):
        rectangle = Rectangle(1, 1, 1, 1, 1)
        rectangle.update(2, 3, 4, 5, 6)
        self.assertEqual(rectangle.id, 2)
        self.assertEqual(rectangle.width, 3)
        self.assertEqual(rectangle.height, 4)
        self.assertEqual(rectangle.x, 5)
        self.assertEqual(rectangle.y, 6)

    def test_update_kwargs(self):
        rectangle = Rectangle(1, 1, 1, 1, 1)
        rectangle.update(width=2, height=3, x=4, y=5, id=6)
        self.assertEqual(rectangle.id, 6)
        self.assertEqual(rectangle.width, 2)
        self.assertEqual(rectangle.height, 3)
        self.assertEqual(rectangle.x, 4)
        self.assertEqual(rectangle.y, 5)

    def test_to_dictionary(self):
        rectangle = Rectangle(4, 5, 1, 2, 10)
        expected_dict = {'id': 10, 'width': 4, 'height': 5, 'x': 1, 'y': 2}
        self.assertEqual(rectangle.to_dictionary(), expected_dict)

if __name__ == '__main__':
    unittest.main()
