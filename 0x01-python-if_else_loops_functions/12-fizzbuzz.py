#!/usr/bin/python3


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0:
            print(f"Fizz", end="")
        if i % 5 == 0:
            print(f"Buzz", end="")
        if i % 3 != 0 and i % 5 != 0:
            print(f"{i}", end="")
        print(" ",end="")
