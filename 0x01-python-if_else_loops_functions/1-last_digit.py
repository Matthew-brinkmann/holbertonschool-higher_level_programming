#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastDig = int(repr(number)[-1])
if lastDig == 0:
    print(f"Last digit of {number} is {lastDig} and is 0")
elif lastDig != 0 and lastDig < 6:
    print(f"Last digit of {number} is {lastDig} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {lastDig} and is greater than 5")
