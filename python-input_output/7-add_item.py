#!/usr/bin/python3
# 7-add_item.py
# Tiffany Walker
""" Function that adds all arguments to a list and saves to file """


import json
from sys import argv
load = __import__('6-load_from_json_file').load_from_json_file
save = __import__('5-save_to_json_file').save_to_json_file

def add_items_to_json():
    """ add existing items from file or create empty list """
    try:
        items = load('add_item.json')
    except FileNotFoundError:
        items = []
    
    for arg in argv[1:]:
        items.append(arg)

    save(items, 'add_item.json')

if __name__ == "__main__":
    add_items_to_json()
