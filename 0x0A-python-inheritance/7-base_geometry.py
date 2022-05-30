#!/usr/bin/python3
"""
module creates a class BaseGeometry
"""


class BaseGeometry:
    """
    class for BaseGeometry
    """
    def area(self):
        """
        causes exception when called
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates Value against rules
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
