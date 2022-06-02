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
        """ init for square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """returns informal representation of string"""
        retStr = f"[{self.__class__.__name__}] ({self.id}) "
        retStr += f"{self.x}/{self.y} - {self.width}"
        return (retStr)

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value
