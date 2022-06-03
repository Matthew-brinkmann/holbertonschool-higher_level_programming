#!/usr/bin/python3
"""
Contains tests for Base class
"""

import unittest
import inspect
import pycodestyle
import json

from models import base
Base = base.Base


class TestBaseDocs(unittest.TestCase):
    """ Tests for documentation of class"""

    @classmethod
    def setUpClass(cls):
        """Set up for the doc tests"""
        cls.base_funcs = inspect.getmembers(Base, inspect.isfunction)

    def test_conformance_class(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_conformance_test(self):
        """Test that we conform to Pycodestyle."""
        style = pycodestyle.StyleGuide(quiet=True)
        result = style.check_files(['tests/test_base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_module_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(base.__doc__) >= 1)

    def test_class_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

    def test_func_docstr(self):
        """Tests for docstrings in all functions"""
        for func in self.base_funcs:
            self.assertTrue(len(func[1].__doc__) >= 1)


class TestBase(unittest.TestCase):
    """ Tests functionality of class"""
    def test_id_none(self):
        """ Tests id as none"""
        b_1 = Base()
        self.assertEqual(b_1.id, 1)

    def test_id_assigned(self):
        """ Tests id is give"""
        b_2 = Base(8)
        self.assertEqual(b_2.id, 8)

    def test_too_many_args(self):
        """ Tests entering too many args to instantiate class"""
        with self.assertRaises(TypeError):
            b = Base(1, 2)

    def test_nb_attribute(self):
        """Tests nb_objects as a private instance attribute"""
        b_3 = Base(3)
        with self.assertRaises(AttributeError):
            print(b_3.nb_objects)
        with self.assertRaises(AttributeError):
            print(b_3.__nb_objects)

    def test_to_json_string(self):
        """Tests to json string"""
        Base._Base__nb_objects = 0
        dictTest1 = {"id": 9, "width": 5, "height": 6, "x": 7, "y": 8}
        dictTest2 = {"id": 2, "width": 2, "height": 3, "x": 4, "y": 0}
        jsonStr = Base.to_json_string([dictTest1, dictTest2])
        self.assertTrue(type(jsonStr) is str)
        newDict = json.loads(jsonStr)
        self.assertEqual(newDict, [dictTest1, dictTest2])

    def test_empty_to_json_string(self):
        """Test for passing empty list/ None"""
        jsonStr = Base.to_json_string([])
        self.assertTrue(type(jsonStr) is str)
        self.assertEqual(jsonStr, "[]")

    def test_None_to_json_String(self):
        """test for None to JSON converter"""
        jsonStr = Base.to_json_string(None)
        self.assertTrue(type(jsonStr) is str)
        self.assertEqual(jsonStr, "[]")
