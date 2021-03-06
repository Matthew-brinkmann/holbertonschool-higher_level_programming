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
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def __str__(self):
        """returns informal representation of string"""
        retStr = f"[{self.__class__.__name__}] ({self.id}) "
        retStr += f"{self.x}/{self.y} - {self.width}/{self.height}"
        return (retStr)

    def to_dictionary(self):
        """ returns a dictionary containing all varaibles"""
        return {'id': self.id,
                'width': self.width,
                'height': self.height,
                'x': self.x,
                'y': self.y}

    def area(self):
        """ returns the area of the rectangle"""
        return (self.width * self.height)

    def display(self):
        """ prints rectangle to stdout"""
        for offy in range(self.y):
            print("")
        for row in range(self.height):
            for offx in range(self.x):
                print("", end=" ")
            for col in range(self.width):
                print('#', end="")
            print("")

    def update(self, *args, **kwargs):
        """ allows update of varaibles"""
        if args is not None and len(args) > 0:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
        elif kwargs is not None:
            for (key, value) in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

    @property
    def width(self):
        """getter for Width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """ setter for Width """
        self.int_validator("width", value)
        self.__width = value

    @property
    def height(self):
        """getter for Height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """ setter for height """
        self.int_validator("height", value)
        self.__height = value

    @property
    def x(self):
        """getter for Width"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """ setter for x"""
        self.int_validator("x", value)
        self.__x = value

    @property
    def y(self):
        """getter for y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """ setter for y"""
        self.int_validator("y", value)
        self.__y = value

    def int_validator(self, attribute, value):
        """ validates data for attributes"""
        if type(value) is not int:
            raise TypeError(f"{attribute} must be an integer")
        if attribute == "width" or attribute == "height":
            if value <= 0:
                raise ValueError(f"{attribute} must be > 0")
        if attribute == "x" or attribute == "y":
            if value < 0:
                raise ValueError(f"{attribute} must be >= 0")
