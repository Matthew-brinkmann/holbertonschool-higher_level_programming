#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        if self.__is_size_correct(size):
            self.__size = size
        if self.__is_position_correct(position):
            self.__position = position

    def area(self):
        return (self.__size * self.__size)

    @property
    def size(self):
        return (self.__size)

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return (self.__position)

    @position.setter
    def position(self, value):
        if self.__is_position_correct(position):
            self.__position = position

    def my_print(self):
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
        if type(size) != int:
            raise TypeError("size must be an integer")
            return (False)
        if size < 0:
            raise ValueError("size must be >= 0")
            return (False)
        else:
            return (True)

    def __is_position_correct(self, position):
        if not isinstance(position, type((0, 0))):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) != int or type(position[1]) != int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            return (True)
