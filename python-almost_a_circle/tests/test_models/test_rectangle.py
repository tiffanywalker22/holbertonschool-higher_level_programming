#!/usr/bin/python3
# test_rectangle.py
# Tiffany Walker

import unittest
from models.rectangle import Rectangle
from models.base import Base

class TestRectangle(unittest.TestCase):
    """ unit tests for rectangle """

    def test_no_args(self):
        """ testing no arguments """
        with self.assertRaises(TypeError):
            Rectangle()

    def test_valid_values(self):
        """ test constructor with valid values """
        rect = Rectangle(5, 10, 15, 20, 1)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 5)
        self.assertEqual(rect.height, 10)
        self.assertEqual(rect.x, 15)
        self.assertEqual(rect.y, 20)

    def test_invalid_width(self):
        """ tests for invalid width type """
        with self.assertRaises(TypeError):
            rect = Rectangle("invalid", 10, 15, 20, 1)

    def test_invalid_height(self):
        """ tests for invalid height type """
        with self.assertRaises(TypeError):
            rect = Rectangle(5, "invalid", 15, 20, 1)

    def test_invalid_x(self):
        """ tests for invalid x type """
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10, "invalid", 20, 1)

    def test_invalid_y(self):
        """ tests for invalid y type """
        with self.assertRaises(TypeError):
            rect = Rectangle(5, 10, 15, "invalid", 1)

    def test_invalid_width_value(self):
        """ test for invalid width value """
        with self.assertRaises(ValueError):
            rect = Rectangle(0, 10, 15, 20, 1)

    def test_invalid_height_value(self):
        """ test for invalid height value """
        with self.assertRaises(ValueError):
            rect = Rectangle(5, 0, 15, 20, 1)

    def test_area(self):
        """ tests the area of rectangle """
        rect = Rectangle(2, 10)
        self.assertEqual(rect.area(), 20)

    def test_str(self):
        """ testing str method """
        rect = Rectangle(5, 10, 15, 20, 1)
        expected_str = "[Rectangle] (1) 15/20 - 5/10"
        self.assertEqual(str(rect), expected_str)

    def test_args(self):
        """ tests the args """
        rect = Rectangle(5, 10, 15, 20, 1)
        rect.update(4, 8, 12, 16, 22)
        self.assertEqual(rect.id, 4)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 12)
        self.assertEqual(rect.x, 16)
        self.assertEqual(rect.y, 22)

    def test_kwargs(self):
        """ tests kwargs """
        rect = Rectangle(5, 10, 15, 20, 1)
        rect.update(id=4, width=8, height=12, x=16, y=22)
        self.assertEqual(rect.id, 4)
        self.assertEqual(rect.width, 8)
        self.assertEqual(rect.height, 12)
        self.assertEqual(rect.x, 16)
        self.assertEqual(rect.y, 22)    
