#!/usr/bin/python3
# 8-rectangle.py
# Tiffany Walker
""" Class Rectanlge using BaseGeometry """
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ The class Rectangle that is inheriting BaseGeometry """
    def __init__(self, width, height):
        self.__width = 0
        self.__height = 0
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height
