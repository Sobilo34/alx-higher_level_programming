#!/usr/bin/python3

import io
import unittest
from unittest.mock import patch
from models.square import Square

class TestSquare(unittest.TestCase):

    def test_init(self):
        square = Square(5, 2, 3, 4)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 4)

    def test_str(self):
        square = Square(5, 2, 3, 4)
        expected_str = "[Square] (4) 2/3 - 5"
        self.assertEqual(str(square), expected_str)

    def test_size_property(self):
        square = Square(5, 2, 3, 4)
        self.assertEqual(square.size, 5)
        square.size = 8
        self.assertEqual(square.size, 8)
        self.assertEqual(square.width, 8)
        self.assertEqual(square.height, 8)

    def test_update(self):
        square = Square(5, 2, 3, 4)
        square.update(10, 7, 8, 9)
        self.assertEqual(square.id, 10)
        self.assertEqual(square.size, 7)
        self.assertEqual(square.x, 8)
        self.assertEqual(square.y, 9)

        square.update(size=15, x=12, y=13)
        self.assertEqual(square.size, 15)
        self.assertEqual(square.x, 12)
        self.assertEqual(square.y, 13)

    def test_to_dictionary(self):
        square = Square(5, 2, 3, 4)
        expected_dict = {'id': 4, 'size': 5, 'x': 2, 'y': 3}
        self.assertEqual(square.to_dictionary(), expected_dict)

    def test_display(self):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            square = Square(3, 2, 1)
            square.display()
            expected_output = '\n  ###\n  ###\n  ###\n\n'  # Include an extra newline character
        self.assertEqual(mock_stdout.getvalue(), expected_output)

# Other test cases and classes go here...

if __name__ == '__main__':
    unittest.main()
