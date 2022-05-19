#!/usr/bin/python3
'''
This module is designed to supply 1 funcion for use
the text_indentation function.
'''


def text_indentation(text):
    '''
    function that prints a text with 2 new lines
    after each of these characters: ., ? and :
    text must be a string
    There should be no space at the beginning or at the end of each printed line
    '''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    lastCharModified = True
    for ch in text:
        if lastCharModified is True:
            if ch == " ":
                continue
            else:
                lastCharModified = False
        if ch == "\n":
                print()
                lastCharModified = True
                continue
        if ch == "." or ch == ":" or ch == "?":
            lastCharModified = True
            print(ch)
            print()
        else:
            print(ch, end="")
