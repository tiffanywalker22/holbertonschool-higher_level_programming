#!/usr/bin/python3
# 4-print_square.py
# Tiffany Walker
""" This function prints a square with # """


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for x in range(size):
            print("#", end="")
        print()
