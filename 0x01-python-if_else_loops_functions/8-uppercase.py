#!/usr/bin/python3


def uppercase(str):
    for ch in str:
        if ord(ch) >= ord('a') and ord(ch) <= ord('z'):
            let = ord(ch) - 32
        else:
            let = ord(ch)
        print(f"{chr(let)}", end="")
    print("")
