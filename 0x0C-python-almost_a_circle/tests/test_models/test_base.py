#!/usr/bin/python3
"""test_base_class module

Contains Tests about the Base class
"""


import unittest
from importlib import reload
from models import base


class TestBaseClass(unittest.TestCase):
    """Class that tests the Base Class
    """

    def setUp(self):
        reload(base)

    def test_class_dict(self):
        """Test whether the normal call works without arguments
        """

        from models.base import Base
        base = Base()
        self.assertEqual(base.__dict__, {'id': 1})

    def test_many_calls(self):
        """Test the class with many calls to the Class instantiations
        """

        from models.base import Base
        base1 = Base()
        self.assertEqual(base1.id, 1)
        base2 = Base()
        self.assertEqual(base2.id, 2)
        base3 = Base(10)
        self.assertEqual(base3.id, 10)
        base4 = Base()
        self.assertEqual(base4.id, 3)

    def test_raising_error(self):
        """Test whether raises errors when accessing private variable and not
        """

        from models.base import Base
        base = Base()
        with self.assertRaises(AttributeError):
            base.__nb_objects
        with self.assertRaises(AttributeError):
            base.nb_objects
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)


if __name__ == '__main__':
    unittest.main()
