#!/usr/bin/python3
"""
Module contains the square class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Class Square, imports from Rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
