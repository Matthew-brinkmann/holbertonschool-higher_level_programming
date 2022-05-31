#!/usr/bin/python3
"""
this module contains 1 class
student
"""


class Student:
    """
    student class representation
    """
    def __init__(self, first_name, last_name, age):
        """
        initialisation for class
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        returns dictionary representation of class
        """
        return (self.__dict__)
