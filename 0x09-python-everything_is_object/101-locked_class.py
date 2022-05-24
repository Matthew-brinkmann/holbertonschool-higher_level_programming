#!/usr/bin/python3
""" Module contains a locked class that only first_name can be
dynamicall used
"""
class LockedClass:
    """A locked class that only lets the user dynamically create the instance
    attribute first_name"""
    __slots__ = ['first_name']
