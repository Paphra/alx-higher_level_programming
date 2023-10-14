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


if __name__ == '__main__':
    unittest.main()
