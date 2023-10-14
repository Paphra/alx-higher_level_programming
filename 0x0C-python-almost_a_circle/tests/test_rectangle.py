#!/usr/bin/python3
"""test_rectangle module

Used to test the Rectangle class that inherits from Base
"""


import unittest
from importlib import reload
from models import base
from models import rectangle


class TestRectangle(unittest.TestCase):
    """Class that tests the Rectangle class
    """

    def setUp(self):
        """Setup the TestCase
        """

        reload(base)
        reload(rectangle)

    def test_rectangle_dict(self):
        """Test the __dict__ contents
        """

        from models.rectangle import Rectangle
        rect = Rectangle(2, 3)
        self.assertEqual(
            rect.__dict__,
            {
                'id': 1,
                '_Rectangle__width': 2,
                '_Rectangle__height': 3,
                '_Rectangle__x': 0,
                '_Rectangle__y': 0
            }
        )

    def test_rectangle_initializations(self):
        """Test the initilization process
        """

        from models.rectangle import Rectangle
        with self.assertRaises(TypeError):
            rect = Rectangle()
        with self.assertRaises(TypeError):
            rect = Rectangle(2)
        rect = Rectangle(3, 2)
        self.assertEqual(type(rect), Rectangle)
        self.assertEqual(rect.id, 1)
        self.assertEqual(rect.width, 3)
        self.assertEqual(rect.height, 2)
        self.assertEqual(rect.x, 0)
        self.assertEqual(rect.y, 0)

    def test_getters_and_setters(self):
        """Test the getters and setters to the intance of the class
        """

        from models.rectangle import Rectangle
        r = Rectangle(3, 4, 5, 6, 10)
        self.assertEqual(r.id, 10)
        self.assertEqual(r.x, 5)
        r.width = 20
        self.assertEqual(r.width, 20)
        r.height = 10
        self.assertEqual(r.height, 10)
        r.id = 14
        self.assertEqual(r.id, 14)

    def test_data_types(self):
        """Test data types of different kinds being set to
        properties of specific types

        This implementation is from Task #3
        """

        from models.rectangle import Rectangle
        r = Rectangle(1, 2, 0, 0, 2)
        with self.assertRaises(TypeError, msg='width must be an integer'):
            r.width = 'w'
        with self.assertRaises(TypeError, msg='height must be an integer'):
            r.height = 'h'
        with self.assertRaises(TypeError, msg='x must be an integer'):
            r.x = 'x'
        with self.assertRaises(TypeError, msg='y must be an integer'):
            r.y = 'y'
        with self.assertRaises(TypeError, msg='width must be an inter'):
            r.width = 0.3
        with self.assertRaises(TypeError, msg='height must be an intger'):
            r.height = True
        with self.assertRaises(TypeError, msg='x must be an integer'):
            r.x = float('inf')
        r.id = 5.6
        self.assertEqual(r.id, 5.6)

    def test_values_checks(self):
        """Test the different value ranges
        """

        from models.rectangle import Rectangle
        r = Rectangle(1, 2, 3, 3, 200)
        with self.assertRaises(ValueError, msg='width must be > 0'):
            r.width = -2


if __name__ == '__main__':
    unittest.main()
