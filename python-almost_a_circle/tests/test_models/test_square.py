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

    def test_values(self):
        """ tests valid values """
        square = Square(2, 4, 6, 1)
        self.assertEqual(square.id, 1)
        self.assertEqual(square.size, 2)
        self.assertEqual(square.x, 4)
        self.assertEqual(square.y, 6)

    def test_invalid_size(self):
        """ test for invalid size """
        with self.assertRaises(TypeError):
            square = Square("invalid", 20, 30, 40, 1)
