#!/usr/bin/python3
"""
module contains
class Metrics
script, to handle class
"""
import sys


class Metrics:
    """
    metrics class to handle holding and display of information
relating to th e
    """
    eCodes = ['200', '301', '400', '401', '403', '404', '405', '500']

    def __init__(self):
        """
        init for metrics class
        sets all attributes to 0(zero) at start
        """
        self.total_size = 0
        self.lineCount = 0
        for code in self.eCodes:
            setattr(self, self.code_to_attr(code), 0)

    def __str__(self):
        """
        informal string for printing data
        """
        if self.total_size == 0:
            return ("")
        retStr = f"File size: {self.total_size}\n"
        for code in self.eCodes:
            value = getattr(self, self.code_to_attr(code))
            if value == 0:
                continue
            retStr += f"{code}: {getattr(self, self.code_to_attr(code))}\n"
        retStr = retStr[:-1]
        return (retStr)

    def code_check(self, Code, size):
        """
        checks if attribute exists and updates fields if required
        """
        if Code in self.eCodes:
            value = getattr(self, self.code_to_attr(Code)) + 1
            setattr(self, self.code_to_attr(Code), value)
            self.total_size += size
        else:
            return

    def code_to_attr(self, Code):
        """
        converts an error code into a string rep of the
        corrisponding attribute
        """
        fullAttr = "e" + Code
        return (fullAttr)


info = Metrics()
try:
    currLine = sys.stdin.readline()
    info.lineCount += 1
    while currLine != "":
        tokens = currLine.split()
        info.code_check(tokens[-2], int(tokens[-1]))
        if (info.lineCount % 10) == 0:
            print(info)
        currLine = sys.stdin.readline()
        info.lineCount += 1
except KeyboardInterrupt:
    print(info)
