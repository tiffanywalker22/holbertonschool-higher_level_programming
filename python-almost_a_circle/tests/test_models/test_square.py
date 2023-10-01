#!/usr/bin/python3
# test_square.py
# Tiffany Walker

import unittest
from models.rectangle import Rectangle
from models.square import Square

class TestSquare(unittest.TestCase):
    """ unit tests for square """

    def test_no_args(self):
        """ testing no arguments """
        with self.assertRaises(TypeError):
            Square()
