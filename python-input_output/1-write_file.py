#!/usr/bin/python3
# 1-write_file.py
# Tiffany Walker
""" Function that writes in a text file """


def write_file(filename="", text=""):
    """ Function that writes a string to text file and
    returns number of characters written """
    with open(filename, mode="w", encoding="utf-8") as file:
        chr_cnt = file.write(text)
    return chr_cnt
