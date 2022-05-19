#!/usr/bin/python3
'''
This module is designed to supply 1 funcion for use
the print_square function.
'''


def print_square(size):
    '''
    function that prints a square with the character #
    size is the size length of the square
    size must be an integer,
    size must be greater than or equal to 0
    '''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    print(("#" * size + "\n") * size, end="")
