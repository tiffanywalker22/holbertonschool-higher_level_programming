#!/usr/bin/python3
# 11-square.py
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

    def __str__(self):
        return (f"[Square] {self.__size}/{self.__size}")
