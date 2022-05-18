#!/usr/bin/python3
'''
The Module is designed supply 1 function for use
add_integer function
'''


def add_integer(a, b=98):
    '''
    The function recieves 2 integers and adds them together,
    and returns the value.
    Values must be integers (will type check)
    Can accept floats, will convert to integers if so.
    '''
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)
