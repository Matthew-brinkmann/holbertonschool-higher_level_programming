#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
x = int(repr(number)[-1])
if x == 0:
    print(f"Last digit of {number} is {x} and is 0")
elif x != 0 and x < 6 or number < 0:
    if number < 0:
        print(f"Last digit of {number} is {-x} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {x} and is less than 6 and not 0")
else:
    print(f"Last digit of {number} is {x} and is greater than 5")
