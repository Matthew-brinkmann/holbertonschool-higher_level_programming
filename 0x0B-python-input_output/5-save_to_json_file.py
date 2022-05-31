#!/usr/bin/python3
"""
module will contain 1 funciton
def save_to_json_file(my_obj, filename):
"""
import json


def save_to_json_file(my_obj, filename):
    """
    deserialises a json rep of python object.
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
