#!/usr/bin/python3
# 9-student.py
# Tiffany Walker
""" function creates class student """


class Student:
    """ Class for Student"""

    def __init__(self, first_name, last_name, age):
        """ initialize first name, last name, age """
        self.first_name = first_name
        self.last_name - last_name
        self.age = age

    def to_json(self):
        return self.__dict__
