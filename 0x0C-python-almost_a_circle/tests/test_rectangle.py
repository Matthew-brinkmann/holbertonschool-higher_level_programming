#!/usr/bin/python3
"""
Contains tests for Base class
"""

import unittest

from models import rectangle
from models.base import Base
Rectangle = rectangle.Rectangle

class TestRectangeDocs(unittest.TestCase):
    """ Tests for documentation of class"""

    def test_module_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(rectangle.__doc__) >= 1)

    def test_class_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

class TestRectangle(unittest.TestCase):
    """ Tests functionality of class"""
    def test_id_none(self):
        """ Tests id as none and heigh and width set"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r1.width, 10)
        self.assertEqual(r1.height, 2)
        self.assertEqual(r1.x, 0)
        self.assertEqual(r1.y, 0)

        r1.x = 10
        r1.y = 10
        self.assertEqual(r1.x, 10)
        self.assertEqual(r1.y, 10)

    def test_id_assigned(self):
        """ Tests id is give"""
        r2 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r2.id, 12)

    def test_too_many_args(self):
        """ Tests entering too many args to instantiate class"""
        with self.assertRaises(TypeError):
            r3 = Rectangle(10, 2, 0, 0, 12, 12)

    def test_too_few_args(self):
        """Tests entering too few args to instantiate object"""
        with self.assertRaises(TypeError):
            r = Rectangle()
