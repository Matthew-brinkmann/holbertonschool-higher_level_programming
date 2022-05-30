#!/usr/bin/python3
"""
module allows for checking inheretance of classes or not
"""


def inherits_from(obj, a_class):
    """
    will return true of false depending
    on relaiton ship between passed objects
    """
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return (True)
    else:
        return (False)
