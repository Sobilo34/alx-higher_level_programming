#!/usr/bin/python3

"""
This function divides all the elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    The function that divides all elements of a matrix.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number to divide all elements of the matrix.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix is not of the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to 0.

    Returns:
        list of lists: A new matrix with elements
        divided by div, rounded to 2 decimal places.
    """
    err_message = "The matrix must be a matrix
    (i.e list of lists) of integers/floats"

    if matrix is None or type(matrix) is not list:
        raise TypeError(err_message)

    if type(matrix[0]) is not list:
        raise TypeError(err_message)

    matrix_len = len(matrix[0])

    for row in matrix:
        if len(row) != matrix_len:
            raise TypeError("Each row of the matrix must have the same size")
        for element in row:
            if type(element) is not int and type(element) is not float:
                raise TypeError(err_message)

    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[] for _ in range(0, len(matrix))]
    counter = 0

    for row in matrix:
        for element in row:
            new_matrix[counter].append(round(element / div, 2))
        counter += 1

    return new_matrix
