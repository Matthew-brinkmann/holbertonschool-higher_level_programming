#!/usr/bin/python3
""" module to define sublass
rectangle, inhereting from baseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    this is  a subclass of baseGeo
    """
    def __init__(self, width, height):
        """
        init for Rectangle, using inherited data_validator
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """
        calculates area of rectangle
        """
        return (self.__width * self.__height)

    def __str__(self):
        """
        enables use of print, creating informal representation of class
        """
        return (f"[Rectangle] {self.__width}/{self.__height}")
