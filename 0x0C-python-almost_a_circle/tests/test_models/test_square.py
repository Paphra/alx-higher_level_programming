#!/usr/bin/python3
"""test_square module

Contains the test to the Square Class
"""


import unittest
import sys
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
