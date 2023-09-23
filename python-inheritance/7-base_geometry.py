#!/usr/bin/python3
# 7-base_geometry.py
# Tiffany Walker
""" The function creates an empty class """


class BaseGeometry:
    """ The empty class """

    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Checks the int value """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
