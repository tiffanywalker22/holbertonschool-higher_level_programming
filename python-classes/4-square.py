#!/usr/bin/python3
# 4-square.py
# Tiffany Walker
"""Defining a class for a Square."""


class Square:
    """The empty class that will define a Square"""

    def __init__(self, size=0):
        """ Initializing the Square"""
        self.__size = size

    def size(self):
        return self.__size

    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ This will print the area of the Square """
        return (self.__size ** 2)
