#!/usr/bin/python3
# 2-is_same_class.py
# Tiffany Walker
""" Function checks if object matches class """


def is_same_class(obj, a_class):
    """ Checks if object is exactly an instance of the specified class """

    return type(obj) == a_class
