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
import io
from contextlib import redirect_stdout

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
        result = style.check_files(['tests/test_models/test_rectangle.py'])
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

    @classmethod
    def setUpClass(cls):
        """ set up all r_ attributes for all tests """
        Base._Base__nb_objects = 0
        cls.r_1 = Rectangle(1, 1)
        cls.r_2 = Rectangle(4, 5)
        cls.r_3 = Rectangle(1, 5, 1, 1, 88)
        cls.r_4 = Rectangle(6, 6)

    def test_properties(self):
        """Tests all setters and getters"""
        self.r_1.x = 0
        self.r_1.y = 0
        self.assertEqual(self.r_1.width, 1)
        self.assertEqual(self.r_1.height, 1)
        self.assertEqual(self.r_1.x, 0)
        self.assertEqual(self.r_1.y, 0)

        self.r_1.x = 10
        self.r_1.y = 10
        self.assertEqual(self.r_1.x, 10)
        self.assertEqual(self.r_1.y, 10)

    """ Tests functionality of super()__init__() call"""

    def test_id_none(self):
        """Tests id not passed in"""
        self.assertEqual(self.r_2.id, 2)

    def test_id_assigned(self):
        """Tests id passed in"""
        self.assertEqual(self.r_3.id, 88)

    def test_nb_object_increment(self):
        """Tests private class attribute incrementation"""
        self.assertEqual(self.r_4.id, 3)

    """Tests number of arguments passed in"""
    def test_too_many_args(self):
        """Tests entering too many args to instantiate object"""
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, 4, 5, 6)

    def test_too_few_args(self):
        """Tests entering too few args to instantiate object"""
        with self.assertRaises(TypeError):
            r = Rectangle()

    def test_string_typeerror(self):
        """Test non-int string validation"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle("hello", 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, "hello")

    def test_boolean_typeerror(self):
        """Test non-int boolean validation"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(True, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, True)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, True)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, True)

    def test_dict_typeerror(self):
        """Test non-int dictionary validation"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle({1, 4}, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, {1, 4})
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, {1, 4})
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, {1, 4})

    def test_list_typeerror(self):
        """Test non-int list validation"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle([2], 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, [2])
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, [2])
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, [2])

    def test_tuple_typeerror(self):
        """ test non-int tuple validation"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle((1,), 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, (1,))
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, (1,))
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, (1,))

    def test_none_typeerror(self):
        """ test non-int None validation"""
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r = Rectangle(None, 1)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r = Rectangle(1, None)
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r = Rectangle(1, 1, None)
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r = Rectangle(1, 1, 1, None)

    def test_width_valueerror(self):
        """Test int validation <= 0 for width"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(-1, 1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r = Rectangle(0, 1)

    def test_height_valueerror(self):
        """Test int validation <= 0 for height"""
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r = Rectangle(1, 0)

    def test_x_valueerror(self):
        """Test int validation < 0 for x"""
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r = Rectangle(1, 1, -1)

    def test_y_valueerror(self):
        """Test int validation <= 0 for y"""
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r = Rectangle(1, 1, 1, -1)

    def test_area(self):
        """test area"""
        self.assertEqual(self.r_1.area(), 1)
        self.assertEqual(self.r_2.area(), 20)
        self.assertEqual(self.r_3.area(), 5)
        self.assertEqual(self.r_4.area(), 36)

    def test_area_args(self):
        """Test too many args for area()"""
        with self.assertRaises(TypeError):
            r = self.r_1.area(1)

    def test_basic_display(self):
        """Test display"""
        with io.StringIO() as buf, redirect_stdout(buf):
            self.r_1.display()
            output = buf.getvalue()
            self.assertEqual(output, "#\n")
        with io.StringIO() as buf, redirect_stdout(buf):
            self.r_2.display()
            output = buf.getvalue()
            self.assertEqual(output, ("#" * 4 + "\n") * 5)

    def test_display_too_many_args(self):
        """Test display with too many args"""
        with self.assertRaises(TypeError):
            self.r_1.display(1)

    def test_str(self):
        """Test the __str__ method"""
        self.x = 10
        self.y = 10
        self.assertEqual(str(self.r_1), "[Rectangle] (1) 10/10 - 1/1")
        self.assertEqual(str(self.r_3), "[Rectangle] (88) 1/1 - 1/5")

    def test_xy_display(self):
        """Test display with xy"""
        self.r_1.x = 2
        self.r_1.y = 2
        self.r_2.x = 8
        self.r_2.y = 4
        with io.StringIO() as buf, redirect_stdout(buf):
            self.r_1.display()
            output = buf.getvalue()
            self.assertEqual(output, "\n" * 2 + (" " * 2 + "#\n"))
        with io.StringIO() as buf, redirect_stdout(buf):
            self.r_2.display()
            output = buf.getvalue()
            self.assertEqual(output, "\n" * 4 + (" " * 8 + "#" * 4 + "\n") * 5)

    def test_update_args(self):
        """Testing the udpate method with *args"""
        self.assertEqual(str(self.r_3), "[Rectangle] (88) 1/1 - 1/5")
        self.r_3.update(99)
        self.assertEqual(str(self.r_3), "[Rectangle] (99) 1/1 - 1/5")
        self.r_3.update(99, 9)
        self.assertEqual(str(self.r_3), "[Rectangle] (99) 1/1 - 9/5")
        self.r_3.update(99, 9, 9)
        self.assertEqual(str(self.r_3), "[Rectangle] (99) 1/1 - 9/9")
        self.r_3.update(99, 9, 9, 9)
        self.assertEqual(str(self.r_3), "[Rectangle] (99) 9/1 - 9/9")
        self.r_3.update(99, 9, 9, 9, 9)
        self.assertEqual(str(self.r_3), "[Rectangle] (99) 9/9 - 9/9")

    def test_update_kwargs(self):
        """Testing the udpate method with *args"""
        self.assertEqual(str(self.r_4), "[Rectangle] (3) 0/0 - 6/6")
        self.r_4.update(id=51)
        self.assertEqual(str(self.r_4), "[Rectangle] (51) 0/0 - 6/6")
        self.r_4.update(x=4, y=9)
        self.assertEqual(str(self.r_4), "[Rectangle] (51) 4/9 - 6/6")
        self.r_4.update(width=7, id=52, height=9)
        self.assertEqual(str(self.r_4), "[Rectangle] (52) 4/9 - 7/9")

    def test_update_setter_usage(self):
        """tests that the update method uses setter with *args"""
        r_5 = Rectangle(1, 1, 0, 0, 1)
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            r.update(1, "hello")
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            r.update(1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            r.update(1, 1, 1, "hello")
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            r.update(1, 1, 1, 1, "hello")
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, 0)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            r.update(1, -1)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 1, 0)
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            r.update(1, 1, -1)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            r.update(1, 1, 1, -1)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            r.update(1, 1, 1, 1, -1)

    def test_dict(self):
        """ tests to_dict method"""
        d1 = self.r_1.to_dictionary()
        self.assertEqual(
            {"id": 1, "width": 1, "height": 1, "x": 0, "y": 0}, d1)
        self.assertTrue(type(d1) is dict)
        self.r_1.x = 5
        self.r_1.y = 2
        d1 = self.r_1.to_dictionary()
        self.assertEqual(
            {"id": 1, "width": 1, "height": 1, "x": 5, "y": 2}, d1)
        self.assertTrue(type(d1) is dict)
