#!/usr/bin/python3
"""
The Module is designed to supply 1 function for use,
the lazy_matrix_mul function using numPy
"""
import numpy


def lazy_matrix_mul(m_a, m_b):
    '''
    this function just uses the numPy funciton matMul
    '''
    return numpy.matmul(m_a, m_b)
