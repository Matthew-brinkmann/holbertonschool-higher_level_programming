#!/usr/bin/python3

def multiple_returns(sentence):
    strLen = len(sentence)
    if strLen == 0:
        return((0, None))
    return((strLen, sentence[0]))
