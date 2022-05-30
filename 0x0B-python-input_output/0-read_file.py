#!/usr/bin/python3
"""
module contains 1 function
def read_file(filename=""):
"""


def read_file(filename=""):
    """
    opens and prints file contents
    to screen.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
