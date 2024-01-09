#!/usr/bin/python3
"""
This is  a class Student that defines a
student by: (based on 9-student.py)
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
        represents of the class of student
        """

        if (type(attrs) is list and
                all(type(elem) is str for elem in attrs)):
            return {e: getattr(self, e) for e in attrs if hasattr(self, e)}
        return self.__dict__
