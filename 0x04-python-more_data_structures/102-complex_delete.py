#!/usr/bin/python3

def complex_delete(a_dictionary, value):
    if value is not None and type(a_dictionary) is dict:
        for (key, val) in list(a_dictionary.items()):
            if val == value:
                del a_dictionary[key]
    return (a_dictionary.copy())
