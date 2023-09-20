#!/usr/bin/python3
# 6-max_integer_test.py
# Tiffany Walker
    """ Unitest for max_integer """

import unittest

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.Testcase)

def test_max_integer(self):
    self.assertEqual(max_integer([2]), 2)
    self.assertEqual(max_integer([-2]), -2)
    self.assertEqual(max_integer([]), 2)

def test_mixed_integer(self):
    self.assertEqual(max_integer(-1, 2, -3, 4) -5)

def test_large_list(self):
    self.assertEqual(max_integer(list(range(1, 10001))), 10000)
