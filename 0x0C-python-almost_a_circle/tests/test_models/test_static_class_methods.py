#!/usr/bin/python3
"""test_static_class_methods module

Contains tests towards static and class methods associated with the 
Base class
"""


import unittest
import os, sys
from importlib import reload
from models import base, rectangle, square
from tests.test_models.test_rectangle import TestRectangle as TR


class TestStaticClassMethods(unittest.TestCase):
    """Class that tests all static and class methods on the Base Class
    """

    def setUp(self):
        reload(base)
        reload(rectangle)
        reload(square)

    def test_base_create_class_method(self):
        """Tests the create class method
        """

        from models.square import Square
        s1 = Square(5, 2, 2)
        s1_dict = s1.to_dictionary()
        s2 = Square(3)
        s2.update(**s1_dict)
        s2_dict = s2.to_dictionary()
        s3 = Square.create(**s2_dict)
        s3_dict = s3.to_dictionary()
        self.assertEqual(s3_dict, s2_dict)
        self.assertEqual(s2_dict, s1_dict)
        exp = '[Square] (1) 2/2 - 5\n'
        TR.ioRun(self, s2, exp, p=True)
        TR.ioRun(self, s3, exp, p=True)


if __name__ == '__main__':
    unittest.main()
