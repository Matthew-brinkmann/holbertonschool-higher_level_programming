#!/usr/bin/python3
"""
module for myInt class to cause some trouble
"""

class MyInt(int):
    """
    reverse  the == and != functionality
    """

    def __eq__(self, other):
        """
        overide == function
        """
        return (int(self) != other)

    def __ne__(self, other):
        """
        overide != function
        """
        return (int(self) == other)
