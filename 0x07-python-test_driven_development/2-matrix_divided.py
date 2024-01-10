#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Function that divides all elements of a matrix.

    Args:
        matrix (list of lists): The matrix to be divided.
        div (int or float): The number to divide all elements of the matrix.

    Raises:
        TypeError: If matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix is not of the same size.
        TypeError: If div is not a number.
        ZeroDivisionError: If div is equal to 0.

    Returns:
        list of lists: A new matrix with elements divided by div, rounded to 2 decimal places.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = [[round(element / div, 2) for element in row] for row in matrix]

    return new_matrix

# Test case
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))
print(matrix)
