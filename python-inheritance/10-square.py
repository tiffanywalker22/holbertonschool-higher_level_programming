#!/usr/bin/python3
# 10-square.py
# Tiffany Walker
""" Class basegeometry, subclass rectangle, subclass square """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Class for Square """

    def __init__(self, size):
        """ Initialize square with size """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
