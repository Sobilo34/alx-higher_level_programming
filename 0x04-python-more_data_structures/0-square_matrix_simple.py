#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    present_matrix = []
    for row in matrix:
        present_row = []
        for element in row:
            present_row.append(element ** 2)
        present_matrix.append(present_row)

    return present_matrix
