#!/usr/bin/python3
# 4-inherits_from.py
# Tiffany Walker
""" Function that determines if object is inherited directly
or indirectly """


def inherits_from(obj, a_class):
    """ Checks if object is inherited directly or
    indirectly from class """
    return issubclass(type(obj), a_class) and type(obj) != a_class
