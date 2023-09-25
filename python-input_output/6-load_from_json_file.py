#!/usr/bin/python3
# 6-load_from_json_file.py
# Tiffany Walker
""" Function that creates an object """


import json


def load_from_json_file(filename):
    """ Creates an object from JSON file """
    with open(filename, encoding="utf-8") as file:
        return json.load(file)
