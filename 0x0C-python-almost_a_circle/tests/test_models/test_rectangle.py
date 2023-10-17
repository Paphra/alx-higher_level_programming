#!/usr/bin/python3
"""test_rectangle module

Used to test the Rectangle class that inherits from Base
"""


import unittest
import sys
import json
from io import StringIO
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
        with self.assertRaises(TypeError, msg='width must be an integer'):
            r = Rectangle('2', 3)
        with self.assertRaises(TypeError, msg='height must be an integer'):
            r = Rectangle(3, '2')
        with self.assertRaises(TypeError, msg='x must be an integer'):
            r = Rectangle(3, 2, '2')
        with self.assertRaises(TypeError, msg='y must be an integer'):
            r = Rectangle(3, 2, 2, '1')

    def test_values_checks(self):
        """Test the different value ranges
        """

        from models.rectangle import Rectangle
        r = Rectangle(1, 2, 3, 3, 200)
        with self.assertRaises(ValueError, msg='width must be > 0'):
            r.width = -2
        with self.assertRaises(ValueError, msg='x must be >= 0'):
            r.x = -3
        r.id = 3.4
        self.assertEqual(r.id, 3.4)
        r.id = float('inf')
        self.assertEqual(r.id, float('inf'))
        with self.assertRaises(ValueError, msg='width must be > 0'):
            r = Rectangle(-1, 2)
        with self.assertRaises(ValueError, msg='height must be > 0'):
            r = Rectangle(2, -3)
        with self.assertRaises(ValueError, msg='width must be > 0'):
            r = Rectangle(0, 2)
        with self.assertRaises(ValueError, msg='height must be > 0'):
            r = Rectangle(2, 0)
        with self.assertRaises(ValueError, msg='x must be >= 0'):
            r = Rectangle(2, 3, -2)
        with self.assertRaises(ValueError, msg='y must be >= 0'):
            r = Rectangle(2, 3, 2, -1)

    def test_area(self):
        """Test the return of the correct area of the rect

        Task #4
        """

        from models.rectangle import Rectangle
        r = Rectangle(5, 6)
        self.assertEqual(r.area(), 30)
        r.width = 3
        r.height = 4
        self.assertEqual(r.area(), 12)

    def test_display(self):
        """Test the out of the Display function
        """

        from models.rectangle import Rectangle
        r = Rectangle(5, 3)
        expected = "#####\n#####\n#####\n"
        self.ioRun(r.display, expected)
        r.width = 4
        r.height = 5
        expected = "####\n####\n####\n####\n####\n"
        self.ioRun(r.display, expected)

    def test_str_magic_method(self):
        """Tests the output of the __str__ method
        """

        from models.rectangle import Rectangle
        r = Rectangle(3, 2, 0, 0, 20)
        expected = "[Rectangle] (20) 0/0 - 3/2\n"
        self.ioRun(r, expected, p=True)
        r.id = 1.4
        r.width = 10
        r.y = 3
        expected = '[Rectangle] (1.4) 0/3 - 10/2\n'
        self.ioRun(r, expected, p=True)

    def test_display_with_xy(self):
        """Test how the xy are handled by the display method
        """

        from models.rectangle import Rectangle
        r = Rectangle(4, 3, 2, 3)
        expected = "\n\n\n  ####\n  ####\n  ####\n"
        self.ioRun(r.display, expected)
        r.x = 3
        r.y = 0
        expected = "   ####\n   ####\n   ####\n"
        self.ioRun(r.display, expected)

    def ioRun(self, entity, expected, p=False):
        """Run IO related tests

        Args:
            entity: some entity, either a callable something to print
            expected: expected Output
            p (bool): a flag to indicate whether the entity is to be printed
                False - callable
                True - printable
        """
        saved = sys.stdout
        try:
            out = StringIO()
            sys.stdout = out
            if p:
                print(entity)
            else:
                entity()
            output = out.getvalue()
            self.assertEqual(output, expected)
        finally:
            sys.stdout = saved

    def test_update(self):
        """Test update method of the rectangle
        """

        from models.rectangle import Rectangle
        r = Rectangle(10, 10)
        r.update(10, 10, 10, 3)
        expected = '[Rectangle] (10) 3/0 - 10/10\n'
        self.ioRun(r, expected, p=True)
        r.update(1, 2, 3, 3, 7)
        expected = '[Rectangle] (1) 3/7 - 2/3\n'
        self.ioRun(r, expected, p=True)

    def test_update_2(self):
        """Test update method that takes both *args and **kwargs
        """

        from models.rectangle import Rectangle
        r = Rectangle(10, 10, 10, 10)
        r.update(height=1)
        expected = '[Rectangle] (1) 10/10 - 10/1\n'
        self.ioRun(r, expected, p=True)
        r.update(width=20, height=20, x=3)
        expected = '[Rectangle] (1) 3/10 - 20/20\n'
        self.ioRun(r, expected, p=True)
        r.update(10, 20, width=25)
        expected = '[Rectangle] (10) 3/10 - 20/20\n'
        self.ioRun(r, expected, p=True)

    def test_rectangle_to_dict(self):
        """Test the conversion of the rectangle to a Dictionary
        """

        from models.rectangle import Rectangle
        r = Rectangle(10, 2, 1, 9)
        dic = r.to_dictionary()
        self.assertEqual(type(dic), dict)
        self.assertEqual(dic, {
            'id': 1,
            'width': 10,
            'height': 2,
            'x': 1,
            'y': 9
        })
        r = Rectangle(1, 1)
        r.update(**dic)
        exp = '[Rectangle] (1) 1/9 - 10/2\n'
        self.ioRun(r, exp, p=True)

    def test_base_to_json_string(self):
        """Tests to_json_string method on the Base class
        """

        from models.square import Square
        from models.base import Base
        s = Square(4)
        s_dict = s.to_dictionary()
        json_dict = Base.to_json_string([s_dict])
        self.assertEqual(json.loads(json_dict)[0], s_dict)
        self.assertEqual(type(json_dict), str)
        json_dict = Base.to_json_string(None)
        self.assertEqual(type(json.loads(json_dict)), list)
        self.assertEqual(json_dict, "[]")
        json_dict2 = Base.to_json_string([])
        self.assertTrue(json_dict == json_dict2)


if __name__ == '__main__':
    unittest.main()
