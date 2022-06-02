#!/usr/bin/python3
"""
Module contains the rectangle class
"""

from models.base import Base

class Rectangle(Base):
    """
    the rectangle class, inherits from Base
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ init fuction """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """getter for Width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """ setter for Width """
        self.__width = value

    @property
    def height(self):
        """getter for Height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """ setter for height """
        self.__height = value

    @property
    def x(self):
        """getter for Width"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """ setter for x"""
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """ setter for y"""
        self.__y = value
