#!/usr/bin/python3

"""
This is a the base class for all other classes in this module.
class constructor: def __init__(self, id=None):
"""

import json
import csv
import turtle
import os


class Base:
    """
    This is the base class
    """
    __nb_objects = 0  # Initializes the private class attribute

    def __init__(self, id=None):
        if id is not None:
            """Assign the public instance attribute
            id with the argument value
            """
            self.id = id
        else:
            """
            Otherwise, increment __nb_objects and assign new
            value to the public instance attribute id
            """
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This return the JSON string representation of list_dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        It writes the JSON string that represent list_objs to a file
        """
        if list_objs is None:
            list_objs = []

        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
                [obj.to_dictionary() for obj in list_objs])

        with open(filename, "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        It returns the list of dictionaries
        from the JSON string representation
        """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        To return an instance with all attributes set
        """
        my_instance = cls(1, 1)  # Creates a an instance with a dummy id
        my_instance.update(**dictionary)
        return my_instance

    @classmethod
    def load_from_file(cls):
        """This is to return a list of instances from a JSON file"""
        filename = "{}.json".format(cls.__name__)
        try:
            with open(filename, mode='r', encoding='utf-8') as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**dic) for dic in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """This is to and serialize and write to CSV file"""
        filename = "{}.csv".format(cls.__name__)
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            if cls.__name__ == 'Rectangle':
                for obj in list_objs:
                    writer.writerow(
                            [obj.id, obj.width, obj.height, obj.x, obj.y])
            elif cls.__name__ == 'Square':
                for obj in list_objs:
                    writer.writerow([obj.id, obj.size, obj.x, obj.y])

    @classmethod
    def load_from_file_csv(cls):
        """This is  to deserialize and read from CSV file"""
        filename = "{}.csv".format(cls.__name__)
        try:
            with open(filename, mode='r', newline='') as file:
                reader = csv.reader(file)
                if cls.__name__ == 'Rectangle':
                    return [cls.create(id=int(row[0]), width=int(
                        row[1]), height=int(row[2]), x=int(row[3]), y=int(
                            row[4])) for row in reader]
                elif cls.__name__ == 'Square':
                    return [cls.create(id=int(row[0]), size=int(
                        row[1]), x=int(row[2]), y=int(
                            row[3])) for row in reader]
        except FileNotFoundError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draws Rectangles and Squares using Turtle graphics"""
        screen = turtle.Screen()
        screen.title("Drawing Rectangles and Squares")
        screen.bgcolor("white")

        for rect in list_rectangles:
            Base._draw_shape(rect.x, rect.y, rect.width, rect.height)

        for sqr in list_squares:
            Base._draw_shape(sqr.x, sqr.y, sqr.size, sqr.size, is_sqr=True)

        turtle.done()

    @staticmethod
    def _draw_shape(x, y, width, height, is_sqr=False):
        """This draws a rectangle or square at the specified position"""
        t = turtle.Turtle()
        t.speed(2)
        t.penup()
        t.goto(x, y)
        t.pendown()

        if is_sqr:
            for _ in range(4):
                t.forward(width)
                t.left(90)
        else:
            for _ in range(2):
                t.forward(width)
                t.left(90)
                t.forward(height)
                t.left(90)
