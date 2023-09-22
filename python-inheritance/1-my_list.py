#!/usr/bin/python3
# 1-my_list.py
# Tiffany Walker
""" Function that creates a class that inherits from list """


class MyList(list):
    """ The class that inherits list """

    def print_sorted(self):
        """ sort/print list """
        sort_list = sorted(self)
        print(sort_list)
