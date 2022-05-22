#!/usr/bin/python3
"""defines a class square"""


class Rectangle:
    """
    following is the class methods and attributs
    for the Rectangle class
    """
    def __init__(self, width=0, height=0):
        """init for class"""
        self.width = width
        self.height = height

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        self.data_validation(value, "width")
        self.__width = value

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        self.data_validation(value, "height")
        self.__height = value

    def data_validation(self, value, attribute):
        if not isinstance(value, int):
            raise TypeError(attribute + " must be an integer")
        if value < 0:
            raise ValueError(attribute + " must be >= 0")
