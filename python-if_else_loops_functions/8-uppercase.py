#!/usr/bin/python3
def uppercase(str):
    new_str = ""
    for letter in str:
        if 97 <= ord(letter) <= 122:
            uppercase = chr(ord(letter) - 32)
            new_str += uppercase
        else:
            new_str += letter
    print("{}".format(new_str))
