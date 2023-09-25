#!/usr/bin/python3
# 7-add_item.py
# Tiffany Walker
""" Function that adds all arguments to a list and saves to file """


import sys
import json
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

def add_items_to_json():
    try:
        items = load_from_json_file('add_item.json')
    except FileNotFoundError:
        items = []
    
    for arg in sys.argv[1:]:
        items.append(arg)

    save_to_json_file(items, 'add_item.json')

if __name__ == "__main__":
    add_items_to_json()
