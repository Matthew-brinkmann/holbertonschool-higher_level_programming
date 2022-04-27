#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

if number < 0:
    hold = -(number)
else:
    hold = number

x = hold % 10

if x == 0:
    string = " and is 0"
elif x != 0 and x < 6 or number < 0:
    if number < 0:
        x = -(x)
    string = " and is less than 6 and not 0"
else:
    string = " and is greater than 5"

print(f"Last digit of {number} is {x}" + string)
