#!/usr/bin/python3
"""
module only contains 1 function
def class_to_json(obj):
"""


def class_to_json(obj):
    """
    returns the dictionary description with simple data structure
    """
    return (obj.__dict__)
