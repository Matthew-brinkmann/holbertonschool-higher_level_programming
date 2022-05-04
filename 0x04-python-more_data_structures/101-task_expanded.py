#!/usr/bin/python3
def square_num_func(x):
    y = x**2
    return y

def row_sort(row):
    new_list = list(map(square_num_func, row))
    return new_list


def square_matrix_map(matrix=[]):
    new_matrix = list(map(row_sort, matrix))
    return (new_matrix)
