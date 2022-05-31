#!/usr/bin/python3
"""
module will contain 1 funciton
def from_json_string(my_str):
"""
import json


def from_json_string(my_str):
    """
    deserialises a json rep of python object.
    """
    return (json.loads(my_str))
