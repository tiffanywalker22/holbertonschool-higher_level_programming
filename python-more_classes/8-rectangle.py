#!/usr/bin/python3
# 8-rectangle.py
# Tiffany Walker
""" Creating an empty class for Rectangle  """


class Rectangle:
    """ Creating a rectangle with width and height """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ Initalize rectangle with width and height """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Retrieves width -- setter method """
        return self.__width

    @width.setter
    def width(self, value):
        """ Sets width -- getter method """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves height -- getter method """
        return self.__height

    @height.setter
    def height(self, value):
        """ Sets height - setter method """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ Return area of rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ Return perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.height)

    def __str__(self):
        """ Returns string representation """
        if self.__width == 0 or self.__height == 0:
            return ""
        rectang_str = ""
        for x in range(self.height):
            rectang_str += str(self.print_symbol) * self.__width + "\n"
        return rectang_str.rstrip()

    def __repr__(self):
        """ Return string representation for repr() """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2
