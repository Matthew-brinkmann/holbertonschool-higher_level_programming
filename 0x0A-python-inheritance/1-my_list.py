#!/usr/bin/python3
"""
module containing a subclass of list
"""


class MyList(list):
    """
    my sublass of a list to provide custom functions
    """
    def print_sorted(self):
        """
        will print the list stored here in accending order
        """
        print(sorted(self))
