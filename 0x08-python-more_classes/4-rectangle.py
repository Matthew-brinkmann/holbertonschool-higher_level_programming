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

    def __str__(self):
        """ returns str representaion of class"""
        string = ""
        if self.width == 0 or self.height == 0:
            return (string)

        for row in range(self.height):
            for col in range(self.width):
                string += '#'
            if row != self.height - 1:
                string += '\n'
        return (string)

    def __repr__(self):
        """ return official sttring representaion of class"""
        string = "Rectangle (" + str(self.width) + ", "
        string += str(self.height) + ")"
        return (string)

    @property
    def width(self):
        """ getter for width attribute"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """ setter for width attribute"""
        self.data_validation(value, "width")
        self.__width = value

    @property
    def height(self):
        """ getter for height attribute"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """ setter for height attribute"""
        self.data_validation(value, "height")
        self.__height = value

    def area(self):
        """ returns area of class"""
        return (self.height * self.width)

    def perimeter(self):
        """ returns area of class"""
        if self.height == 0 or self.width == 0:
            return (0)
        else:
            return ((self.height * 2) + (self.width * 2))

    def data_validation(self, value, attribute):
        """ data_validation method for all attributes"""
        if not isinstance(value, int):
            raise TypeError(attribute + " must be an integer")
        if value < 0:
            raise ValueError(attribute + " must be >= 0")
