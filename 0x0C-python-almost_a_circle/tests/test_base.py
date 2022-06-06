#!/usr/bin/python3
"""
Contains tests for Base class
"""

import unittest
import inspect
import pycodestyle
import json
import os

from models.rectangle import Rectangle
from models.square import Square
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
        Base._Base__nb_objects = 0
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

    def test_write_file(self):
        """tests write to file"""
        s1 = Square(1, 1, 1, 1)
        s2 = Square(2, 2, 2, 2)
        r1 = Rectangle(3, 3, 3, 3, 3)
        r2 = Rectangle(4, 4, 4, 4, 4)
        junk = {"id": 123, "width": 5, "height": 5, "x": 2, "y": 4}
        Square.save_to_file([s1, s2])
        with open('Square.json', 'r', encoding='utf-8') as f:
            text = f.read()
        textAsDicts = eval(text)
        self.assertEqual(textAsDicts[0]['id'], 1)
        self.assertEqual(textAsDicts[1]['x'], 2)

        Rectangle.save_to_file([r1, r2])
        with open('Rectangle.json', 'r', encoding='utf-8') as f:
            text = f.read()
        textAsDicts = eval(text)
        self.assertEqual(textAsDicts[0]['id'], 3)
        self.assertEqual(textAsDicts[1]['x'], 4)

        Rectangle.save_to_file([junk, r1, r2])
        with open('Rectangle.json', 'r', encoding='utf-8') as f:
            text = f.read()
        textAsDicts = eval(text)
        self.assertEqual(textAsDicts[0]['id'], 3)
        self.assertEqual(textAsDicts[1]['x'], 4)

    def test_empty_from_JSON_str(self):
        """Tests for None from JSON converter"""
        self.assertEqual([], Base.from_json_string(""))

    def test_None_from_JSON_str(self):
        """Test for passing empty string"""
        self.assertEqual([], Base.from_json_string(None))

    def test_create_square(self):
        """tesrt create method for square class"""
        s = Square(1, 2, 3, 4)
        sqDict = s.to_dictionary()
        s2 = Square.create(**sqDict)
        self.assertEqual(s.id, s2.id)
        self.assertEqual(s.y, s2.y)
        self.assertEqual(s.x, s2.x)
        self.assertEqual(s.size, s2.size)

    def test_create_rectangle(self):
        """test create method for rectangle"""
        r = Rectangle(1, 2, 3, 4, 5)
        reDict = r.to_dictionary()
        r2 = Rectangle.create(**reDict)
        self.assertEqual(r.id, r2.id)
        self.assertEqual(r.y, r2.y)
        self.assertEqual(r.x, r2.x)
        self.assertEqual(r.height, r2.height)
        self.assertEqual(r.width, r2.width)

    def test_read_from_file(self):
        """tests the read from file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list_rectangles_output[0].y, 8)
        self.assertEqual(list_rectangles_output[1].height, 4)

    def test_empty_read_from_file(self):
        """tests the read from file method with empty file"""
        try:
            os.remove('Square.json')
        except Exception:
            pass
        list_output = Square.load_from_file()
        self.assertEqual(len(list_output), 0)
        self.assertEqual(list, type(list_output))

    def test_write_csv_file(self):
        """tests write to file"""
        s1 = Square(1, 1, 1, 1)
        s2 = Square(2, 2, 2, 2)
        r1 = Rectangle(3, 3, 3, 3, 3)
        r2 = Rectangle(4, 4, 4, 4, 4)
        Square.save_to_file_csv([s1, s2])
        with open('Square.csv', 'r', encoding='utf-8') as f:
            text = f.readlines()
        self.assertEqual(text[0][0], "1")
        self.assertEqual(text[1][0], "2")

        Rectangle.save_to_file_csv([r1, r2])
        with open('Rectangle.csv', 'r', encoding='utf-8') as f:
            text = f.readlines()
        self.assertEqual(text[0][0], "3")
        self.assertEqual(text[1][0], "4")

    def test_read_from_csv(self):
        """tests the read from csv file method"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file_csv(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file_csv()
        self.assertEqual(list_rectangles_output[0].y, 8)
        self.assertEqual(list_rectangles_output[1].height, 4)

    def test_empty_read_from_csv(self):
        """ tests the read from csv file methods with empty file"""
        try:
            os.remove('Square.csv')
        except Exception:
            pass
        list_output = Square.load_from_file_csv()
        self.assertEqual(0, len(list_output))
        self.assertEqual(list, type(list_output))
