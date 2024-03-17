#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os
from unittest.mock import patch, mock_open

class TestBase(unittest.TestCase):

    def test_id_increment(self):
        """
        This is the unittest that tests if an id is
        incremented at every new instance of Base
        """
        instance_1 = Base()
        instance_2 = Base()
        self.assertEqual(instance_1.id, 3)  # Test if id is incremented by 1
        self.assertEqual(instance_2.id, 4)  # Tests if id is incremented by another 1

    def test_id_correctness(self):
        """
        This is the unittest that tests the correctness of an id when passed as an argument to Base
        """
        base_instance = Base(100)
        self.assertEqual(base_instance.id, 100)

    def test_mixed_instance(self):
        """
        This is to test if id is incremented for different classes
        """
        base_instance = Base()
        rectg_instance = Rectangle(5, 10)
        square_instance = Square(3)
        self.assertEqual(base_instance.id, 7)  # check increment of base, no argument for base
        self.assertEqual(rectg_instance.id, 8)  # check increment for rectangle
        self.assertEqual(square_instance.id, 9)  # check increment of square

    def test_to_json_string(self):
        """
        This is to test if JSON representation is succesful
        """
        # Test with an empty list
        content = Base.to_json_string([])
        self.assertEqual(content, "[]")

        # Test with a non-empty list
        data = [{'key1': 'val1'}, {'key2': 'val2'}]
        content = Base.to_json_string(data)
        output = '[{"key1": "val1"}, {"key2": "val2"}]'
        self.assertEqual(content, output)

        # Test with None input
        content = Base.to_json_string(None)
        self.assertEqual(content, "[]")

    def test_from_json_string(self):
        """
        This is to test the from_json method
        """
        # Test with an empty list
        content = Base.from_json_string("[]")
        self.assertEqual(content, [])

        # Test with non-empty list
        data = '[{"key1": "val1"}, {"key2": "val2"}]'
        content = Base.from_json_string(data)
        output = [{'key1': 'val1'}, {'key2': 'val2'}]
        self.assertEqual(content, output)

        # Test with none input
        content = Base.from_json_string(None)
        self.assertEqual(content, [])

    def test_save_to_file(self):
        """
        This is test if JSON is writtent to
        the expected file successfully
        """
        # Test with an empty list
        file_name = "Rectangle.json"
        Rectangle.save_to_file([])
        with open(file_name, 'r') as file:
            content = file.read()
        output = '[]'
        self.assertEqual(content, output)

        # Test with a non-empty list
        my_rectangles = [Rectangle(1, 2, 3, 4), Rectangle(5, 6, 7, 8)]
        Rectangle.save_to_file(my_rectangles)
        with open(file_name, 'r') as file:
            content = file.read()

        for each in my_rectangles:
            self.assertIn(f'{{"id": {each.id}, "width": {each.width}, "height": {each.height}, "x": {each.x}, "y": {each.y}}}', content)

        os.remove(file_name)

    def test_create(self):
        # This id to test the create method
        instance = Base.create(id=1, width=2, height=3, x=4, y=5)
        self.assertIsInstance(instance, Base)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.width, 2)
        self.assertEqual(instance.height, 3)
        self.assertEqual(instance.x, 4)
        self.assertEqual(instance.y, 5)

    @patch('builtins.open', new_callable=mock_open, read_data='[{"id": 1}]')
    @patch('models.base.Base.from_json_string', return_value=[{'id': 1}])
    def test_load_from_file(self, mock_from_json_string, mock_open):
        """
        This is to test load_from_file method
        """
        # Call the method you are testing
        result = Base.load_from_file()

        # Make assertions based on the expected behavior
        mock_open.assert_called_once_with('Base.json', mode='r', encoding='utf-8')
        mock_from_json_string.assert_called_once_with('[{"id": 1}]')

        # Compare relevant attributes of instances
        expected_instance = Base(id=1)
        self.assertEqual(result[0].id, expected_instance.id)

    @patch('builtins.open', side_effect=FileNotFoundError)
    def test_load_from_file_file_not_found(self, mock_open):
        """
        Test the load_from_file method when the file is not found
        """
        instances = Base.load_from_file()
        mock_open.assert_called_once_with('Base.json', mode='r', encoding='utf-8')
        self.assertEqual(instances, [])

if __name__ == '__main__':
    unittest.main()
