#!/usr/bin/python3

"""
Create a function def pascal_triangle(n): that returns
a list of lists of integers representing
the Pascal’s triangle of n
Prototype: def pascal_triangle(n): 
"""


def pascal_triangle(n):
    """
    The function that generates pascal trinagle
    Argumnet:
            n - The number of rows to generate
    """
    if n <= 0:
        return []
    if n == 1:
        return [[1]]

    triangle = []
    for a in range(n):
        row = [1]

        if a > 1:
            prev = triangle[a - 1]
            for b in range(1, a):
                new = prev[b - 1] + prev[b]
                row.append(new)

        if a > 0:
            row.append(1)

        triangle.append(row)

    return triangle
