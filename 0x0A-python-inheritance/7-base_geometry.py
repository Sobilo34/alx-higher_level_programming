#!/usr/bin/python3
"""
a class BaseGeometry (based on 6-base_geometry.py)
"""


class BaseGeometry: 
     """ 
     A class that defines the geometry 
     """ 
     def area(self): 
         """ 
         unimplemented area function 
         """ 
         raise Exception("area() is not implemented") 
  
     def integer_validator(self, name, value): 
         """ 
         integer validation 
         Args 
            name: name of value 
            value: value 
         Must be an int greater than 0 
         """ 
         if type(value) is not int: 
             raise TypeError("{} must be an integer".format(name)) 
  
         if value <= 0: 
             raise ValueError("{} must be greater than 0".format(name))
