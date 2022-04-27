#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    string1 = "{} argument".format(argc)
    if argc == 0:
        string1 += 's.'
    elif argc == 1:
        string1 += ':'
    else:
        string1 += 's:'

    print(string1)

    i = 0
    for arg in sys.argv:
        if i != 0:
            print(f"{i}: {arg}")
        i += 1
