#!/usr/bin/python3
# 2-append_write.py
# Tiffany Walker
""" Function that writes in a text file """


def append_write(filename="", text=""):
    with open(filename, mode="a", encoding="utf-8") as file:
        chr_cnt = file.write(text)
    return chr_cnt 
