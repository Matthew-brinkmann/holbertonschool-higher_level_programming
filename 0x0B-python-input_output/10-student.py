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

    def to_json(self, attrs=None):
        """
        returns dictionary representation of class
        """
        if attrs is None:
            return (self.__dict__)

        retDict = {}
        if type(attrs) is list:
            for i in range(len(attrs)):
                if type(attrs[i]) != str:
                    return self.__dict__

        for a in attrs:
            if a in self.__dict__:
                retDict[a] = self.__dict__[a]
        return (retDict)
