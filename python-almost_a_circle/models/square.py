#!/usr/bin/python3
# square.py
# Tiffany Walker
""" file for class square """


from models.rectangle import Rectangle


class Square(Rectangle):
    """ the class for sqaure """

    def __init__(self, size, x=0, y=0, id=None):
        """ initalizing the square """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ returns string rep of square """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ getter - return size of sqaure """
        return self.width

    @size.setter
    def size(self, value):
        """ setter - sets width and height """
        self.width = value
        self.height = value
