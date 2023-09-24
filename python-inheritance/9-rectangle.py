#!/usr/bin/python3
# 9-rectangle.py
# Tiffany Walker
""" Class Rectanlge using BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ The class Rectangle that is inheriting BaseGeometry """

    def __init__(self, width, height):
        """ Initialize rectangle width and height """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ Returns area of rectangle """
        return self.__width * self.__height

    def __str__(self):
        return (f"[Rectangle] {self.__width}/{self.__height}")
