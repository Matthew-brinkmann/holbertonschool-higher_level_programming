#!/usr/bin/python3
"""
Module to add attribute to compatible classes/ objects
"""


def add_attribute(obj, name, value):
    """
    runs check on data, then if object is compatible,
    adds attribute to class
    """
    if hasattr(obj, "__dict__") is False:
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
