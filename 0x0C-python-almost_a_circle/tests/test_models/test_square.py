#!/usr/bin/python3
"""test_square module

Contains the test to the Square Class
"""


import unittest
import sys
import json
import os
from importlib import reload
from models import base
from models import rectangle
from models import square
from tests.test_models.test_rectangle import TestRectangle as TR


class TestSquare(unittest.TestCase):
    """A test case to test all the instance of the Square Class
    """

    def setUp(self):
        """Setup the tests, reseting the modules
        """

        reload(base)
        reload(rectangle)
        reload(square)

    def test_square_initialization(self):
        """Tests the initialization of the Square class
        """

        from models.square import Square
        s = Square(20)
        expected = '[Square] (1) 0/0 - 20\n'
        TR.ioRun(self, s, expected, p=True)

    def test_square_updates_via_direct_assignment(self):
        """Tests the assignment to properties
        """

        from models.square import Square
        s = Square(10)
        s.x = 3
        expected = '[Square] (1) 3/0 - 10\n'
        TR.ioRun(self, s, expected, p=True)

    def test_square_updates_to_size(self):
        """Test the getter and setter of the size property
        """

        from models.square import Square
        s = Square(20)
        s.size = 2
        expected = '##\n##\n'
        TR.ioRun(self, s.display, expected)
        s.size = 3
        s.x = 2
        s.y = 2
        expected = '\n\n  ###\n  ###\n  ###\n'
        TR.ioRun(self, s.display, expected)

    def test_square_size_updates_raises(self):
        """Test exception raising following the Rectangle's
        """

        from models.square import Square
        s = Square(2)
        with self.assertRaises(TypeError, msg='width must be an integer'):
            s.size = 'w'
        with self.assertRaises(ValueError, msg='width must be > 0'):
            s.size = 0

    def test_square_update(self):
        """Tests the update method of the Square class
        """

        from models.square import Square
        s = Square(10, 2, 2)
        exp = '[Square] (1) 2/2 - 10\n'
        TR.ioRun(self, s, exp, p=True)
        s.update(10, 3, 3)
        exp = '[Square] (10) 3/2 - 3\n'
        TR.ioRun(self, s, exp, p=True)
        s.update(5, 2, size=5)
        exp = '[Square] (5) 3/2 - 2\n'
        TR.ioRun(self, s, exp, p=True)
        s.update(size=4, x=2, y=3)
        exp = '\n\n\n  ####\n  ####\n  ####\n  ####\n'
        TR.ioRun(self, s.display, exp)

    def test_square_to_dict(self):
        """Tests the to_dictionary method of the square class
        """
        from models.square import Square
        s = Square(20, 3, 3)
        dic = s.to_dictionary()
        self.assertEqual(dic, {
            'id': 1,
            'size': 20,
            'x': 3,
            'y': 3
        })
        self.assertEqual(type(dic), dict)
        TR.ioRun(self, s, '[Square] (1) 3/3 - 20\n', p=True)
        s2 = Square(2)
        s2.update(**dic)
        TR.ioRun(self, s2, '[Square] (1) 3/3 - 20\n', p=True)
        self.assertFalse(s == s2)

    def test_base_save_to_file(self):
        """Tests the Base class method that writes a list of instances

        to a file
        """

        from models.square import Square
        from models.base import Base
        s1 = Square(3)
        s2 = Square(2)
        s1_json = s1.to_dictionary()
        s2_json = s2.to_dictionary()
        json_string = Base.to_json_string([s1_json, s2_json])
        exp_json = [
            {'id': 1, 'size': 3, 'x': 0, 'y': 0},
            {'id': 2, 'size': 2, 'x': 0, 'y': 0}
        ]
        Square.save_to_file([s1, s2])
        tmp_file = 'Rectangle.json'
        if os.path.exists(tmp_file):
            os.remove(tmp_file)
        with self.assertRaises(FileNotFoundError):
            with open(tmp_file, 'r') as file:
                pass
        f_name = '{}.json'.format(Square.__name__)
        with open(f_name, 'r') as f:
            contents = f.read()
            TR.ioRun(self, contents, '{}\n'.format(json_string), p=True)
            self.assertEqual(contents, json_string)
            self.assertEqual(json.loads(contents), exp_json)
        os.remove(f_name)

    def test_base_from_json_string(self):
        """Tests from_json_string method of Base class
        """

        from models.square import Square
        i_list = [
            {'id': 4, 'size': 5},
            {'id': 2, 'size': 3}
        ]
        i_json = Square.to_json_string(i_list)
        o_list = Square.from_json_string(i_json)
        self.assertEqual(json.loads(i_json), o_list)
        self.assertEqual(type(o_list), list)
        self.assertEqual(i_list, o_list)
