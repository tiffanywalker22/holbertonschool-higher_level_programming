#!/usr/bin/python3
# 10-student.py
# Tiffany Walker
""" function creates class student """


class Student:
    """ Class for Student"""

    def __init__(self, first_name, last_name, age):
        """ initialize first name, last name, age """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
    
    def to_json(self, attrs=None):
        """ Gets a dictionary representation of student """
        if attrs is None:
            return self.__dict__
        else:
            result = {
                attr: getattr(self, attr)
                for attr in attrs if hasattr(self, attr)
            }
            return result
