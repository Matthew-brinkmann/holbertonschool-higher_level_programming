#!/usr/bin/python3
"""
module contains 1 function
def pascal_triangle(n):
"""


def pascal_triangle(n):
    """
    will print a pascal triangle the size of n
    """
    retList = []
    if n <= 0:
        return (retList)

    for i in range(n):
        if i == 0 or i == 1:
            retList.append([1 for q in range(0, i + 1)])
        else:
            currLine = []
            for j in range(0, len(retList[i - 1]) + 1):
                if j == 0 or j == len(retList[i - 1]):
                    currLine.append(1)
                else:
                    currLine.append(retList[i - 1][j - 1] + retList[i - 1][j])
            retList.append(currLine)

    return (retList)
