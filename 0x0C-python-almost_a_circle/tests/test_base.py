#!/usr/bin/python3
"""
Contains tests for Base class
"""

import unittest

from models import base
Base = base.Base


class TestBaseDocs(unittest.TestCase):
    """ Tests for documentation of class"""

    def test_module_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(base.__doc__) >= 1)

    def test_class_docstr(self):
        """ Tests for docstring"""
        self.assertTrue(len(Base.__doc__) >= 1)

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
