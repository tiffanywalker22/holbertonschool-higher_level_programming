#!/usr/bin/python3
# 8-rectangle.py
# Tiffany Walker
""" Class Rectanlge using BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ The class Rectangle that is inheriting BaseGeometry """

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
