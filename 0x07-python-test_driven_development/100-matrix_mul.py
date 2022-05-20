#!/usr/bin/python3
'''
Module to return the product of 2 matrices
contains seperate functions for data validation
3 seperate functions for type validation
2 seperate functions for value validation
'''

def matrix_mul(m_a, m_b):
    '''
    function that multiplies 2 matrices:
    (m_a) * (m_b)
    This is the entry intou our function, however most of the exception checking
    is done in other functions, if all exceptions pass, then this function
    runs the multiplication.
    does check if the valuse (m_a) and (m_b) are lists.
    '''
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    if not is_matrix(m_a):
        raise TypeError("m_a must be a list of lists")
    if not is_matrix(m_b):
        raise TypeError("m_b must be a list of lists")

    if not is_not_empty(m_a):
        raise ValueError("m_a can't be empty")
    if not is_not_empty(m_b):
        raise ValueError("m_b can't be empty")

    if not contains_correct_datatype(m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not contains_correct_datatype(m_b):
        raise TypeError("m_b should contain only integers or floats")

    if not matrix_is_rectangle(m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not matrix_is_rectangle(m_b):
        raise TypeError("each row of m_b must be of the same size")

    if not can_be_multiplied(m_a, m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    newRows = len(m_a)
    newCols = len(m_b[0])
    ret = []
    for row_i in range(newRows):
        values = []
        for col_i in range(newCols):
            res = 0
            for j in range(len(m_a[row_i])):
                res += m_a[row_i][j] * m_b[j][col_i]
            values.append(res)
        ret.append(values)
    return ret


def is_matrix(matrix):
    '''
    checks if a list is a list of lists (aka a matrix)
    '''
    return (all(isinstance(ele, list) for ele in matrix))


def is_not_empty(matrix):
    '''
    checks if the matrix, or any of it's sub lists are empty
    '''
    if (matrix is None or len(matrix) == 0):
        return False
    for i in matrix:
        if (i is None or len(i) == 0):
            return False
    return True

def contains_correct_datatype(matrix):
    '''
    checks if the matrix only contains integers of float
    '''
    for row in matrix:
        for ele in row:
            if not isinstance(ele, (int, float)):
                return False
    return True


def matrix_is_rectangle(matrix):
    '''
    checks if all rows are equal in matrix
    '''
    prevRowLen = -1
    for row in matrix:
        if prevRowLen != -1 and prevRowLen != len(row):
            return False
        prevRowLen = len(row)
    return True


def can_be_multiplied(m_a, m_b):
    '''
    checks if 2 matrix can be multiplied
    number of rows in 1 matrix is equal to
    columns in other matrix.
    '''
    return (len(m_a[0]) == len(m_b))
