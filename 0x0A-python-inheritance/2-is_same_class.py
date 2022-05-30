#!/usr/bin/python3
"""
module allows for checking of same classes or not
"""


def is_same_class(obj, a_class):
    """
    will return true of false depending
    on relaiton ship between passed objects
    """
    return (type(obj) == a_class)
