#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Returns a list of lists representing Pascal's triangle of n.

    Args:
        n (int): The number of rows of Pascal's triangle to generate

    Returns:
        list: Empty list if n <= 0, otherwise list of lists representing
              Pascal's triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]
        current_row = [1]

        for j in range(1, i):
            current_row.append(prev_row[j-1] + prev_row[j])

        current_row.append(1)

        triangle.append(current_row)

    return triangle
