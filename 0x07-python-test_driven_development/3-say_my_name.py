#!/usr/bin/python3
'''
This module is designed to supply 1 funcion for use:
say_my_name function.
'''


def say_my_name(first_name, last_name=""):
    '''
    function that prints My name is (first name) (last name)
    First Name must be a string
    Lasat Name must be a string
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print(f"My name is {first_name} {last_name}")
