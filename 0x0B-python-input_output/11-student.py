#!/usr/bin/python3
"""This is a class Student that defines a student by:
    (based on 9-student.py)
"""


class Student:
    """ Declaration of the Student class """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        This is to get a dictionary that
        represents of the student class
        """

        if (type(attrs) is list and
                all(type(element) is str for element in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        for i, value in json.items():
            setattr(self, i, value)
