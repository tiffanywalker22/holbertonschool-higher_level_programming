#!/usr/bin/python3
# 6-max_integer_test.py
# Tiffany Walker
""" Unitest for max_integer """


import unittest

max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ Class for unittest """

    def test_max_integer(self):
        self.assertEqual(max_integer([2]), 2)
        self.assertEqual(max_integer([-2]), -2)
        self.assertNotEqual(max_integer([]), 2)
        self.assertNotEqual(max_integer([2]), -2)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([1, 4, 7, 8]), 8)
        self.assertEqual(max_integer([4, 14, 7, 8]), 14)

    def test_mixed_integer(self):
        self.assertEqual(max_integer([-1, 2, -3, -5]), 2)
        self.assertEqual(max_integer([-2, 3, -4, -6]), 3)

    def test_large_list(self):
        self.assertEqual(max_integer(list(range(1, 10001))), 10000)

if __name__ == '__main__':
    unittest.main()
