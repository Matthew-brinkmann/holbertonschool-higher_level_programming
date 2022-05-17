#!/usr/bin/python3
"""defines a class square"""


class Square:
    """
    class for Square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Init class with args: size && position
        runs a check to ensure size data is correct type and value.
        runs checks to ensure position is the correct data types.
        """
        if self.__is_size_correct(size):
            self.__size = size
        if self.__is_position_correct(position):
            self.__position = position

    def __str__(self):
        """
        str returns linked list values as a string
        so that it can be used in a print statement.
        """
        str = ""
        if self.__size == 0:
            str += '\n'
            return (str)
        for i in range(self.__position[1]):
            str += '\n'
        i = 0
        for i in range(self.__size):
            y = 0
            x = 0
            for y in range(self.__position[0]):
                str += ' '
            for x in range(self.__size):
                str += '#'
            if i < (self.__size - 1):
                str += '\n'
        return (str)

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

    @property
    def position(self):
        """
        Returns the value stored in the private variable position
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        sets the private variable of postion
        runs a check to ensure size data is correct type and values.
        """
        if self.__is_position_correct(value):
            self.__position = value

    def my_print(self):
        """
        Prints the square to the stdout.
        no takes into account the position variable.
        """
        if self.__size == 0:
            print()
            return
        for i in range(self.__position[1]):
            print()
        i = 0
        for i in range(self.__size):
            y = 0
            x = 0
            for y in range(self.__position[0]):
                print(" ", end="")
            for x in range(self.__size):
                print("#", end="")
            print()

    def __is_size_correct(self, size):
        """
        this is a private method to check if the inputted size
        is correct value and type.
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
            return (False)
        if size < 0:
            raise ValueError("size must be >= 0")
            return (False)
        else:
            return (True)

    def __is_position_correct(self, position):
        """
        this is a private method to check if the
        inputted position is correct value and type.
        """
        if not isinstance(position, type((0, 0))) or len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            return (True)
