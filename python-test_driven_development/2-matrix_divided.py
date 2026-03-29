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
    new_matrix = []
    for i in range(0, len(matrix)):
        if not type(i) == list:
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
        row = []
        for j in range(0, len(matrix[i])):
            if not type(matrix[i][j]) in [int, float]:
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            row.append(round(matrix[i][j] / div, 2))
        new_matrix.append(row)
    return new_matrix
