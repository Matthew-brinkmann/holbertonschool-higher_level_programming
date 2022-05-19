#!/usr/bin/python3
'''
This moduel is designed to supply 1 funcion for use
the matrix_divided function
'''


def matrix_divided(matrix, div):
    '''
    Function recieves:
    - a matrix (matrix)
    - number to divide(div) each matrix item by.
    Matrix items must be int or float and can be negative
    Each matrix row must be the same size
    Div must be int or float, & can't be 0
    results must be 2 decimal places
    '''

    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    ret = []
    try:
        first_len = len(matrix[0])
    except IndexError:
        return (ret)

    if type(matrix) is not list:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    for i in matrix:
        line_list = []
        if type(i) is not list:
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats")
        if first_len != len(i):
            raise TypeError("Each row of the matrix must have the same size")
        for j in i:
            if not isinstance(j, int) and not isinstance(j, float):
                raise TypeError(
                    "matrix must be a matrix (list of lists) of \
integers/floats")
            line_list.append(round(j / div, 2))
        ret.append(line_list)
    return (ret)
