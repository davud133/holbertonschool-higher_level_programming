#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in range(0, len(matrix)):
        for d in range(0, len(matrix[i])):
            print("{:d} ".format(matrix[i][d]) end="" if d < len(matrix[i]) - 1 else "{:d}\n".format(matrix[i][d]))
        print()
