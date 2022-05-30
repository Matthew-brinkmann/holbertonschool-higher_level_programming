#!/usr/bin/python3


def add_attribute(obj, name, value):
    if hasattr(obj, "__dict__") == False:
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
