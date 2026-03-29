#!/usr/bin/python3
"""this module contains function for divide matrices"""


def matrix_divided(matrix, div):
    """ returns a new matrix which elements are matrix's elements divided by div"""
    if not type(matrix) == list:
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not type(div) in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    for i in matrix:
        if len(i) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    new_matrix = matrix.copy()
    for i in range(0, len(new_matrix)):
        for j in range(0, len(new_matrix[i])):
            if not type(new_matrix[i][j]) in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            new_matrix[i][j] = round(new_matrix[i][j] / div, 2)
    return new_matrix
