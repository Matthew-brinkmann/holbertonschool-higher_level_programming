#!/usr/bin/python3
"""
module contains 1 funciton
def append_after(filename="", search_string="", new_string=""):
"""


def append_after(filename="", search_string="", new_string=""):
    """
    will search filename, for string_search, and if it finds a match
    will insert new_sting in a new_line
    """

    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    retList = []
    for line in lines:
        retList.append(line)
        if search_string in line:
            retList.append(new_string)

    with open(filename, 'w', encoding='utf-8') as f:
        f.writelines(retList)
