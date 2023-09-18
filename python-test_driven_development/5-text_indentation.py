#!/usr/bin/python3
# 5-text_indentation.py
# Tiffany Walker
""" This function prints text with 2 new lines after each of these 
    characters ., /, and : """


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    punc_chrs = ['.', '?', ':']

    line = ""
    for chr in text:
        line += chr

        if chr in punc_chrs:
            print(line.strip())
            print("")
            line = ""
    if line:
        print(line.strip())
