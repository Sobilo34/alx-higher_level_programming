#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import os

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
        self.assertEqual(base_instance.id, 5)  # check increment of base, no argument for base
        self.assertEqual(rectg_instance.id, 6)  # check increment for rectangle
        self.assertEqual(square_instance.id, 7)  # check increment of square

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

    def setUp(self):
        # set up some initial conditions or mock objects here
        pass

    def tearDown(self):
        # clean up any resources after each test
        pass

    def test_create(self):
        # This id to test the create method
        instance = Base.create(id=1, width=2, height=3, x=4, y=5)
        self.assertIsInstance(instance, Base)
        self.assertEqual(instance.id, 1)
        self.assertEqual(instance.width, 2)
        self.assertEqual(instance.height, 3)
        self.assertEqual(instance.x, 4)
        self.assertEqual(instance.y, 5)

    def test_load_from_file(self):
        # Test the load_from_file method
        # You might need to create a dummy file with known content for this test
        # Ensure the content is consistent with your test expectations
        pass

    def test_save_to_file_csv(self):
        # Test the save_to_file_csv method
        # You might need to create some instances and call the method, then check the file content
        pass

    def test_load_from_file_csv(self):
        # Test the load_from_file_csv method
        # You might need to create a dummy CSV file with known content for this test
        # Ensure the content is consistent with your test expectations
        pass

    def test_draw(self):
        # Test the draw method
        # This method interacts with the Turtle graphics library and might be challenging to test
        # You may want to use mocking to isolate the behavior
        pass

    def test__draw_shape(self):
        # Test the _draw_shape method
        # Similar to the draw method, this interacts with the Turtle graphics library
        # Consider using mocking to isolate the behavior
        pass
if __name__ == '__main__':
    unittest.main()
