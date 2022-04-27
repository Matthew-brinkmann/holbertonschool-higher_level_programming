#!/usr/bin/python3
for i in range(0, 9):
    for x in range(i + 1, 10):
        print(f"{i}{x}", end='')
        if i != 8:
            print(", ", end='')
        else:
            print("")
