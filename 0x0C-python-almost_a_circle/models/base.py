#!/usr/bin/python3
"""
Module contains Class Base:
"""


class Base:
    """
    parent class to square and rectangle to handle
    the id attribute of all child classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        init for Base Class
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id
