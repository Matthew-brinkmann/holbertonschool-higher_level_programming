#!/usr/bin/python3
"""
Contains tests for Rectangle class - Task 2
Focus is on:
- setting private instance attributes in the constructor using
  getters and setters
- calling super()__init__() to set public instance id attribute
"""

import unittest
import inspect
import pycodestyle

from models.base import Base
from models import rectangle
Rectangle = rectangle.Rectangle


class TestRectangleDocs(unittest.TestCase):
    """Tests for documentation of class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.rect_funcs = inspect.getmembers(Rectangle, inspect.isfunction)

    def test_conformance_class(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_conformance_test(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstr(self):
        """Tests for docstring"""
        self.assertTrue(len(rectangle.__doc__) >= 1)

    def test_class_docstr(self):
        """Tests for docstring"""
        self.assertTrue(len(Rectangle.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for docstrings in all functions"""
        for func in self.rect_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestRectangle(unittest.TestCase):
    """ Tests functionality of class"""

    def test_properties(self):
        """Tests all setters and getters"""
        Base._Base__nb_objects = 0
        r_1 = Rectangle(1, 1)
        self.assertEqual(r_1.width, 1)
        self.assertEqual(r_1.height, 1)
        self.assertEqual(r_1.x, 0)
        self.assertEqual(r_1.y, 0)

        r_1.x = 10
        r_1.y = 10
        self.assertEqual(r_1.x, 10)
        self.assertEqual(r_1.y, 10)

    """ Tests functionality of super()__init__() call"""

    def test_id_none(self):
        """Tests id not passed in"""
        r_2 = Rectangle(1, 1)
        self.assertEqual(r_2.id, 2)

    def test_id_assigned(self):
        """Tests id passed in"""
        r_3 = Rectangle(1, 1, 1, 1, 88)
        self.assertEqual(r_3.id, 88)

    def test_nb_object_increment(self):
        """Tests private class attribute incrementation"""
        r_4 = Rectangle(1, 1)
        self.assertEqual(r_4.id, 3)

    """Tests number of arguments passed in"""
    def test_too_many_args(self):
        """Tests entering too many args to instantiate object"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 4, 5, 6)

    def test_too_few_args(self):
        """Tests entering too few args to instantiate object"""
        with self.assertRaises(TypeError):
            r = Rectangle()
