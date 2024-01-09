#!/usr/bin/pyhton3

"""
THis is a function that Write a class Student that defines a student
"""

class Student:
    """
    class that defines a Student
    """
def __init__(self, first_name, last_name, age):
    """
    Initilize the class
    """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        This will retrieve dictionary that represents student
        """
        return self.__dict__
