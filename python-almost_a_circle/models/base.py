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
    def from_json_string(json_string):
        """ return list of dictionaries rep by json_string"""
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save json str of list_objs to file """
        filename = cls.__name__ + ".json"
        json_objects = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(json_objects)

        with open(filename, "w") as file:
            file.write(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ return a list of instances """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ return list of instances from file """
        filename = cls.__name__ + ".json"
        instance_list = []

        try:
            with open(filename, "r") as file:
                json_string = file.read()
                dictionaries = cls.from_json_string(json_string)
                for dictionary in dictionaries:
                    instance = cls.create(**dictionary)
                    instance_list.append(instance)
        except FileNotFoundError:
            pass
        return instance_list
