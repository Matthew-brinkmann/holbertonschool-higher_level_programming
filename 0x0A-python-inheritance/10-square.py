#!/usr/bin/python3
""" module to define sublass
square, inhereting from baseGeometry and
Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    this is  a subclass of baseGeo and rectangle
    """
    def __init__(self, size):
        """
        init for square, using inherited data_validator
        and setting, using __init___ for parent class Rectangle
        so we can use the __str__ functions
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """
        calculates area of square
        """
        return (self.__size ** 2)
