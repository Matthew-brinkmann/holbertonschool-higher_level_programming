#!/bin/usr/python3

def print_matrix_integer(matrix=[[]]):
    mat_height = len(matrix)
    for i in range(mat_height):
        mat_len = len(matrix[i])
        for j in range(mat_len):
            if j != mat_len - 1:
                endchar = ' '
            else:
                endchar = ''
            print(f"{matrix[i][j]}", end=endchar)
        print("")
