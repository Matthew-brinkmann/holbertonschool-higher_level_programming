#!/usr/bin/python3
"""defines a class square"""


class Rectangle:
    """
    following is the class methods and attributs
    for the Rectangle class
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """init for class"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """ returns str representaion of class"""
        string = ""
        if self.width == 0 or self.height == 0:
            return (string)

        for row in range(self.height):
            for col in range(self.width):
                string += str(self.print_symbol)
            if row != self.height - 1:
                string += '\n'
        return (string)

    def __repr__(self):
        """ return official sttring representaion of class"""
        string = "Rectangle (" + str(self.width) + ", "
        string += str(self.height) + ")"
        return (string)

    def __del__(self):
        """ will be called with class is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

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
        if attribute == "width" or attribute == "height":
            if not isinstance(value, int):
                raise TypeError(attribute + " must be an integer")
            if value < 0:
                raise ValueError(attribute + " must be >= 0")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ compares 2 rectangle objects"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return (rect_2)
        else:
            return (rect_1)

    @classmethod
    def square(cls, size=0):
        """ create a square using rectangle class"""
        return (cls(size, size))
