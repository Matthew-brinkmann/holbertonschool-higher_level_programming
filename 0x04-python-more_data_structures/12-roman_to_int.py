#!/usr/bin/python3
def roman_to_int(roman_string):
    romConv = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    retVal = 0
    intHold = []
    if roman_string is None or type(roman_string) is not str:
        return 0
    for ch in roman_string:
        addVal = romConv.get(ch)
        if addVal is None:
            return 0
        else:
            intHold.append(addVal)
    for i in range(len(intHold)):
        if i != (len(intHold) - 1):
            if intHold[i] < intHold[i + 1]:
                intHold[i] = -intHold[i]
        if len(intHold) < 4:
            if i < (len(intHold) - 2):
                if intHold[i] < intHold[i + 2]:
                    intHold[i] = -intHold[i]
    retVal = sum(intHold)
    return int(retVal)
