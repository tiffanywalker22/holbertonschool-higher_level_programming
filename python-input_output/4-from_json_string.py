#!/usr/bin/python3
# 4-from_json_string.py
# Tiffany Walker
""" Function that returns an object represented by JSON """


import json


def from_json_string(my_str):
    """ return an object represented by json string """
    return json.loads(my_str)
