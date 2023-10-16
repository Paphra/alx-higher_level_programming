#!/usr/bin/python3
"""test_static_class_methods module

Contains tests towards static and class methods associated with the
Base class
"""


import unittest
import os
import sys
import json
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

    def test_base_load_from_file(self):
        """Tests the load_from_file class method of Base class
        """

        from models.square import Square
        from models.rectangle import Rectangle

        s_file = 'Square.json'
        r_file = 'Rectangle.json'
        if os.path.exists(s_file):
            os.remove(s_file)
        if os.path.exists(r_file):
            os.remove(r_file)

        s1 = Square(5)
        s2 = Square(3, 0, 3)
        si_list = [s1, s2]
        Square.save_to_file(si_list)
        sf_list = Square.load_from_file()
        self.assertEqual(type(sf_list), list)
        self.assertEqual(sf_list[0].id, si_list[0].id)
        TR.ioRun(self, sf_list[1], '[Square] (2) 0/3 - 3\n', p=True)

        r1 = Rectangle(3, 2)
        r2 = Rectangle(4, 2, 2, 2)
        ri_list = [r1, r2]
        Rectangle.save_to_file(ri_list)
        rf_list = Rectangle.load_from_file()
        self.assertEqual(type(rf_list), list)
        self.assertEqual(rf_list[0].id, ri_list[0].id)
        TR.ioRun(self, rf_list[1], '[Rectangle] (6) 2/2 - 4/2\n', p=True)

        os.remove(s_file)
        Square.save_to_file(None)
        o_list = Square.load_from_file()
        self.assertEqual(type(o_list), list)
        self.assertTrue(len(o_list) == 0)
        self.assertEqual(o_list, [])

        os.remove(r_file)
        Rectangle.save_to_file([])
        o_list = Rectangle.load_from_file()
        self.assertEqual(type(o_list), list)
        self.assertTrue(len(o_list) == 0)
        self.assertEqual(o_list, [])

        os.remove(s_file)
        os.remove(r_file)

        o_list = Rectangle.load_from_file()
        self.assertEqual(type(o_list), list)
        self.assertTrue(len(o_list) == 0)
        self.assertTrue(o_list == [])

    def test_base_save_load_to_from_file_csv(self):
        """Tests saving to and loading from csv file
        """

        from models.square import Square
        from models.rectangle import Rectangle

        s_file = 'Square.csv'
        r_file = 'Rectangle.csv'
        if os.path.exists(s_file):
            os.remove(s_file)
        if os.path.exists(r_file):
            os.remove(r_file)

        s1 = Square(5)
        s2 = Square(3, 0, 3)
        si_list = [s1, s2]
        Square.save_to_file_csv(si_list)
        sf_list = Square.load_from_file_csv()
        self.assertEqual(type(sf_list), list)
        self.assertEqual(sf_list[0].id, si_list[0].id)
        TR.ioRun(self, sf_list[1], '[Square] (2) 0/3 - 3\n', p=True)

        r1 = Rectangle(3, 2)
        r2 = Rectangle(4, 2, 2, 2)
        ri_list = [r1, r2]
        Rectangle.save_to_file_csv(ri_list)
        rf_list = Rectangle.load_from_file_csv()
        self.assertEqual(type(rf_list), list)
        self.assertEqual(rf_list[0].id, ri_list[0].id)
        TR.ioRun(self, rf_list[1], '[Rectangle] (6) 2/2 - 4/2\n', p=True)

        os.remove(s_file)
        Square.save_to_file_csv(None)
        o_list = Square.load_from_file_csv()
        self.assertEqual(type(o_list), list)
        self.assertTrue(len(o_list) == 0)
        self.assertEqual(o_list, [])

        os.remove(r_file)
        Rectangle.save_to_file_csv([])
        o_list = Rectangle.load_from_file_csv()
        self.assertEqual(type(o_list), list)
        self.assertTrue(len(o_list) == 0)
        self.assertEqual(o_list, [])

        os.remove(s_file)
        os.remove(r_file)

        o_list = Rectangle.load_from_file_csv()
        self.assertEqual(type(o_list), list)
        self.assertTrue(len(o_list) == 0)
        self.assertTrue(o_list == [])


if __name__ == '__main__':
    unittest.main()
