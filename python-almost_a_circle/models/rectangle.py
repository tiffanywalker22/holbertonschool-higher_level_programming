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
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ returns height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter method for height of rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ returns x coordinate"""
        return self.__x

    @x.setter
    def x(self, value):
        """ setter method for x"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
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
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """ calculates and returns the area """
        return self.__width * self.__height

    def display(self):
        """ prints rectangle with # char """
        for x in range(self.__y):
            print()
        for x in range(self.__height):
            print(" " * self.__x + "#" * self.width)

    def __str__(self):
        """ returns string """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - " \
            f"{self.__width}/{self.__height}"

    def update(self, *args):
        """ assigns args to each attribute """
        arg_count = len(args)
        if arg_count > 0:
            self.id = args[0]
        if arg_count > 1:
            self.width = args[1]
        if arg_count > 2:
            self.height = args[2]
        if arg_count > 3:
            self.x = args[3]
        if arg_count > 4:
            self.y = args[4]
