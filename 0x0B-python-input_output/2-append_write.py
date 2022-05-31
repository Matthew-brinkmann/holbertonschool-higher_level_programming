#!/usr/bin/python3
"""
module contains 1 function
def write_file(filename="", text=""):
"""


def append_write(filename="", text=""):
    """
    function will write to file
    """
    with open(filename, 'a', encoding='utf=8') as f:
        return f.write(text)
