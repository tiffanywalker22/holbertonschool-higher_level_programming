#!/usr/bin/python3
# 3-to_json_string.py
# Tiffany Walker
""" Function that returns the JSON representation of an object """


import json


def to_json_string(my_obj):
    """ Return JSON representation of obj """
    return json.dumps(my_obj)
