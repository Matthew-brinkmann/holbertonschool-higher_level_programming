#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    '''
    unittest class for testing max_integer function.
    '''
    def test_module_documentation(self):
        '''test for module documentation'''
        test = __import__('6-max_integer').__doc__
        self.assertTrue(len(test) > 1)

    def test_module_function(self):
        '''test for function documentation'''
        test = max_integer.__doc__
        self.assertTrue(len(test) > 1)

    def test_positive_int_start(self):
        '''test result of positive int in list at start'''
        test = [60, 2, 23, 54, 15]
        self.assertEqual(max_integer(test), 60)

    def test_positive_int_middle(self):
        '''test result of positive int in list in mid'''
        test = [3, 2, 6, 4, 5]
        self.assertEqual(max_integer(test), 6)

    def test_positive_int_end(self):
        '''test result of positive int in list at end'''
        test = [16, 22, 35, 41, 60]
        self.assertEqual(max_integer(test), 60)

    def test_mixed_int(self):
        '''test result of mixed int in list'''
        test = [16, 22, -35, 41, -60]
        self.assertEqual(max_integer(test), 41)

    def test_negative_ints(self):
        '''test result of negative int in list'''
        test = [-16, -1, -35, -41, -60]
        self.assertEqual(max_integer(test), -1)

    def test_tuple_pass(self):
        '''test result of pass tuple'''
        test = (41, 60)
        self.assertEqual(max_integer(test), 60)

    def test_empty_list(self):
        """tests result of empty list []"""
        test = []
        self.assertIsNone(max_integer(test))

    def test_None_pass(self):
        '''test resutlf of passing None'''
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_string_pass(self):
        '''test result of pass string'''
        test = [-16, -1, "Holberton", -41, -60]
        with self.assertRaises(TypeError):
            max_integer(test)


if __name__ == "__main__":
    unittest.main()
