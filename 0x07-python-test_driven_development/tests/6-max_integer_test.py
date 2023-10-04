#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxIntegerFunction(unittest.TestCase):
    """
    The test case
    """

    def test_empty_list(self):
        self.assertTrue(max_integer([]) is None)

    def test


if __name__ == '__main__':
    unittest.main()
