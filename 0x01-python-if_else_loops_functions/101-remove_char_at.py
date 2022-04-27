#!/usr/bin/python3


def remove_char_at(str, n):
    loop = 0
    strCpy = ""
    for ch in str:
        if loop == n:
            loop += 1
            continue
        strCpy += ch
        loop += 1
    return strCpy
