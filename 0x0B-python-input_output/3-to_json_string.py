#!/usr/bin/python3
"""
module will contain 1 funciton
def to_json_string(my_obj):
"""
import json


def to_json_string(my_obj):
    """
    will return a json rep of python object.
    """
    return (json.dumps(my_obj))
