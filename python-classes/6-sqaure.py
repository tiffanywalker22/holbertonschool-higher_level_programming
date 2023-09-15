#!/usr/bin/python3
# 6-square.py
# Tiffany Walker
"""Defining a class for a Square."""


class Square:
    """The empty class that will define a Square"""

    def __init__(self, size=0, position=(0, 0)):
        """ Initializing the Square"""
        self.__size = size
        self.position = position

    @property
    def size(self):
        """ Getter method; finds size """
        return self.__size

    @size.setter
    def size(self, value):
        """ Setter method; sets value of size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ Getter method; finds the position """
        return self.__position

    @position.setter
    def position(self, value):
        """ Setter method; sets value for the position """
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(isinstance(x, int) for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not all(x >= 0 for x in value):

            self.__position = value

    def area(self):
        """ This will print the area of the Square """
        return (self.__size ** 2)

    def my_print(self):
        """ This prints the shape of Square """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
