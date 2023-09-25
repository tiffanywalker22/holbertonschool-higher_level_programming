#!/usr/bin/python3
# 5-save_to_json_file.py
# Tiffany Walker
""" Function that writes an object to txt file """


import json


def save_to_json_file(my_obj, filename):
    """ function that writes object to file in json representation """
    with open(filename, mode="w", encoding="utf-8") as file:
        json.dump(my_obj, file)
