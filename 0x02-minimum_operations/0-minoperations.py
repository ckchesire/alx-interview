#!/usr/bin/python3
"""This module is used to calculate the minimum number of operations needed
to achieve exactly 'n' characters in a text file beginning with a single 'H'.
The only operations allowed are Copy and Paste.
"""


def minOperations(n):
    """
    Compute the minimum number of operations to achieve exactly 'n'
    characters in this file, starting with one 'H' and using only Copy All and
    Paste operations

    Args:
        n (int) : Target number of characters

    Returns:
        int : minimum number of operations required to reach 'n' characters
    """
    if n < 2:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
