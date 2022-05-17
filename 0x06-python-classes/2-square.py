#!/usr/bin/python3
"""defines a class square"""


class Square:
    """
    class for Square
    """
    def __init__(self, size=0):
        """
        Init class with args: size
        runs a check to ensure size data is correct type and value.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
