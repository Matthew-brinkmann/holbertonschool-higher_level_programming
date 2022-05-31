#!/usr/bin/python3
"""
module contains 1 function
def write_file(filename="", text=""):
"""


def write_file(filename="", text=""):
    """
    function will write to file
    """
    with open(filename, 'w', encoding='utf=8') as f:
        return f.write(text)
