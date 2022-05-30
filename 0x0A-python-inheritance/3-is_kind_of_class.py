#!/usr/bin/python3
"""
module allows for checking of instances classes or not
"""


def is_kind_of_class(obj, a_class):
    """
    will return true of false depending
    on relaiton ship between passed objects
    """
    return (isinstance(obj, a_class))
