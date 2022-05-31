#!/usr/bin/python3
"""
module will contain 1 funciton
def load_from_json_file(filename):
"""
import json


def load_from_json_file(filename):
    """
    loads json and return a python Object
    """
    with open(filename, 'r', encoding='utf-8') as f:
        return (json.load(f))
