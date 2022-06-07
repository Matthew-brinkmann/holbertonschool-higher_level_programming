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

    def to_dictionary(self):
        """ returns dicitonary of current attributes"""
        sqDict = super().to_dictionary()
        del sqDict['height']
        newKeys = {"id": "id", "width": "size", "x": "x", "y": "y"}
        return (dict([(newKeys.get(key), val) for key, val in sqDict.items()]))

    def update(self, *args, **kwargs):
        """ allows update of varaibles"""
        if args is not None and len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                elif i == 1:
                    self.size = arg
                elif i == 2:
                    self.x = arg
                elif i == 3:
                    self.y = arg
        elif kwargs is not None:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    @property
    def size(self):
        """getter for size"""
        return self.width

    @size.setter
    def size(self, value):
        """setter for size"""
        self.width = value
        self.height = value
