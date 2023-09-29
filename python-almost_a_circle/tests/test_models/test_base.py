#!/usr/bin/python3
# test_base.py
# Tiffany Walker

import unittest
from models.base import Base

class TestBase(unittest.TestCase):
    """ unit testing base.py  """

    def test_id(self):
        """ test if id is correct """
        obj = Base(22)
        self.assertEqual(obj.id, 22)

    def test_no_input(self):
        """ test for no input """
        obj = Base()
        self.assertEqual(obj.id, 1)
