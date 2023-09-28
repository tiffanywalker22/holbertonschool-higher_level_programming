#!/usr/bin/python3
# rectangle.py
# Tiffany Walker
""" file for class rectangle """


from models.base import Base


class Rectangle(Base):
    """ class for rectangle """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initialize width, height, x, and y """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ returns width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter method for width of rectangle """
        if value <= 0:
            raise ValueError("Width must be greater than 0")
        self.__width = value

    @property
    def height(self):
        """ returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method for height of rectangle """
        if value <= 0:
            raise ValueError("Height must be greater than 0")
        self.__height = value

    @property
    def x(self):
        """ returns x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """ setter method for x"""
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ returns y coordinate """
        return self.__y

    @y.setter
    def y(self, value):
        """ setter method for y """
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value
