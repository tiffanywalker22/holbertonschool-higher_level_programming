#!/usr/bin/python3
# 0-add_integer.py
# Tiffany Walker
""" This function adds 2 integers """


def add_integer(a, b=98):
    """ This function adds two integers and can convert floats to ints """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    
    a = int(a)
    b = int(b)

    return a + b
