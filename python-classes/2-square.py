#!/usr/bin/python3
# 2-sqaure.py
# Tiffany Walker
"""Defining a class for a Square."""


class Square:
    """The empty class that will define a Square"""

    def __init__(self, size=0):
        """ Initializing the Square"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
