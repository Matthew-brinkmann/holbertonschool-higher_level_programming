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
    lastCharSpace = False
    isStartOfLine = True
    spaceCounter = 0
    newStr = ""
    for ch in text:
        if isStartOfLine is True:
            if ch == " ":
                continue
            else:
                isStartOfLine = False
        if lastCharSpace is True:
            if ch == " ":
                spaceCounter += 1
                continue
            elif ch == "\n":
                isStartOfLine = True
                lastCharSpace = False
                newStr += ch
                spaceCounter = 0
                continue
            else:
                lastCharSpace = False
                newStr += (" " * spaceCounter)
                spaceCounter = 0
        if ch == "." or ch == ":" or ch == "?":
            newStr += ch
            newStr += "\n\n"
            isStartOfLine = True
        elif ch == " ":
            spaceCounter += 1
            lastCharSpace = True
        else:
            if ch == "\n":
                isStartOfLine = True
            newStr += ch

    print(newStr, end="")
