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
        pass


if __name__ == '__main__':
    unittest.main()
