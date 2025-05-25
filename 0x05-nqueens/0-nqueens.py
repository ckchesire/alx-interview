#!/usr/bin/python3
"""
The N queens  puzzle challenge.

-  Aim to place N non-attacking queens on an NxN chessboard

Usage a user should call the program as follows.
-> nqueens N
 so if len(sys.argv) < 2:
        print("Usage: nqueens N")
        sys.exit(1)
"""
import sys


def cmd_line() -> int:
    """
    Method that takes in command line arguments

    Args:
       None

    Returns:
       Returns an integer variable representing N
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    return int(sys.argv[1])


def is_safe(queens, row, col):
    """
    Checks whether placing a queen at (row, col) is safe.
    """
    for r in range(row):
        c = queens[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_n_queens(N):
    """
    Solves the N queens puzzle using backtracking.

    Returns:
        list: list of solutions, each as a list of [row, col] pairs
    """
    def backtrack(row, queens):
        """
        Bactracking implementation to search every possible path, to
        find all valid complete solution.
        """
        if row == N:
            soln = [[r, queens[r]] for r in range(N)]
            solns.append(soln)
            return
        for col in range(N):
            if is_safe(queens, row, col):
                queens.append(col)
                backtrack(row + 1, queens)
                queens.pop()

    solns = []
    backtrack(0, [])
    return solns


if __name__ == "__main__":
    N = cmd_line()
    solns = solve_n_queens(N)
    for soln in solns:
        print(soln)
