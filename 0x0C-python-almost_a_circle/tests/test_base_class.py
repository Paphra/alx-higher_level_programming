#!/usr/bin/python3
"""test_base_class module

Contains Tests about the Base class
"""


import unittest


from models.base import Base

class TestBaseClass(unittest.TestCase):
    """Class that tests the Base Class
    """

    def test_class_dict(self):
        """Test whether the normal call works without arguments
        """
        base = Base()
        self.assertEqual(base.__dict__, {'id': 1})

    def test_many_calls(self):
        """Test the class with many calls to the Class instantiations
        """
        base1 = Base()
        self.assertEqual(base1.id, 2)
        base2 = Base()
        self.assertEqual(base2.id, 3)
        base3 = Base(10)
        self.assertEqual(base3.id, 10)
        base4 = Base()
        self.assertEqual(base4.id, 4)

    def test_raising_error(self):
        """Test whether raises errors when accessing private variable and not
        """

        base = Base()
        with self.assertRaises(AttributeError):
            base.__nb_objects
        with self.assertRaises(AttributeError):
            base.nb_objects
        with self.assertRaises(AttributeError):
            print(Base.__nb_objects)


if __name__ == '__main__':
    unittest.main()
