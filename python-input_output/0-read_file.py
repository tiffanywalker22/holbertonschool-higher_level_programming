#!/usr/bin/python3
# 0-read_file
# Tiffany Walker
""" Function that reads a text file """


def read_file(filename=""):
    """ Function reads file and prints to stdout"""
    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line, end="")
