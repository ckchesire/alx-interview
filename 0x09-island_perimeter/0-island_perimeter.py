#!/usr/bin/python3
"""
Module to compute and return the perimeter of an island.
"""


def nearest_neighbours(grid, i, j):
    """Method to check the neighbouring land sections part of the island.

       Args:
         grid: 2D matrix representation of the island.
         i (int): integer value representing row number.
         j (int): integer value representing column number.

       Return:
         counter (int): return counter of the neighbouring land setions.
    """
    counter = 0

    if (i > 0 and grid[i-1][j]):
        counter += 1

    if (j > 0 and grid[i][j+1]):
        counter += 1

    if (i > 0 and grid[i+1][j]):
        counter += 1

    if (j > 0 and grid[i][j-1]):
        counter += 1
    return counter


def island_perimeter(grid):
    """Method to calculate the island perimeter based on the grid.

       Args:
         grid(int): 2D matrix representation of the island.

       Return:
         perimeter(int): returns the perimeter of the island.
    """
    row = len(grid)
    col = len(grid[0])
    perimeter = 0

    for r in range(row):
        for c in range(col):
            if grid[r][c] == 1:
                perimeter += 4 - nearest_neighbours(grid, r, c)
    return perimeter
