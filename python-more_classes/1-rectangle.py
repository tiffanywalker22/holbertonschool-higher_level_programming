#!/usr/bin/python3
# 1-rectangle.py
# Tiffany Walker
""" Creating an empty class for Rectangle  """


class Rectangle:
    """ Creating a rectangle with width and height """

def __init__(self, width=0, height=0):
    """ Initalize rectangle with width and height """
    self.width = width
    self.height = height

@property
def width(self):
    """ Retrieves width -- setter method """
    return self.__width

@width.setter
def width(self, value):
    """ Sets width -- getter method """
    if not isinstance(value, int):
        raise TypeError("width must be an integer")
    if value < 0:
        raise ValueError("width must be >= 0")
    self.__width = value

    @property
    def height(self):
        """Retrieves height -- getter method """
        return self.__height
    
    @height.setter
    def height(self, value):
        """ Sets height - setter method """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
