#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1
    result = 0
    if argc == 0:
        print(f"{result}")
        exit()

    i = 0
    for arg in sys.argv:
        if i != 0:
            result += int(arg)
        else:
            i += 1
    print(f"{result}")
