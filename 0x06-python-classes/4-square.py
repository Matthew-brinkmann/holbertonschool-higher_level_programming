#!/usr/bin/python3
"""defines a class square"""


class Square:
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

    def area(self):
        """
        returns the area size of the square
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """
        Returns the value stored in the private variable size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        sets the private variable of size
        runs a check to ensure size data is correct type and value.
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value
