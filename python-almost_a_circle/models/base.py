#!/usr/bin/python3
# base.py
# Tiffany Walker
""" Our base class for all other clases """


import json


class Base:
    """ Our class 'base' """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return json rep of list_dictionaries """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"
        json_objects =  [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(json_objects)

        with open(filename, "w") as file:
            file.write(json_string)
