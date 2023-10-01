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

    def update(self, *args, **kwargs):
        """ assigns attrubutes to square """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """ returns dictionary rep of square """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
            }
