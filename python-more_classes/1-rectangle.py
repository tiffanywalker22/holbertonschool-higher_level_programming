#!/usr/bin/python3
# 0-rectangle.py
# Tiffany Walker
""" Creating an empty class for Rectangle  """


class Rectangle:
    """ Creating a rectangle with width and height """

def __init__(self, width=0, height=0):
    """ Initalize rectangle with width and height """
    self.width = width
    self.height = height

def width(self):
    return self.__width

def width(self, value):
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self.__width = value

    def height(self):
        return self.__height
    
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
        