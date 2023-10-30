#!/usr/bin/python3
"""
N-queens puzzle solver
"""

import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen at board[row][col]
    """
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper-left diagonal
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check if there is a queen in the upper-right diagonal
    i = row - 1
    j = col + 1
    while i >= 0 and j < len(board):
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1

    return True


def solve_nqueens(board, row, solutions):
    """
    Recursive function to solve the N-queens problem using backtracking
    """
    if row == len(board):
        # All queens have been successfully placed
        # Add the solution to the list of solutions
        solution = []
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 1:
                    solution.append([i, j])
        solutions.append(solution)
        return

    for col in range(len(board)):
        if is_safe(board, row, col):
            # Place the queen in the current position
            board[row][col] = 1

            # Recur for the next row
            solve_nqueens(board, row + 1, solutions)

            # Backtrack and remove the queen from the current position
            board[row][col] = 0


def print_solutions(solutions):
    """
    Print the solutions to the N-queens problem
    """
    for solution in solutions:
        print(solution)


def main():
    """
    Main function
    """
    # Check the number of arguments
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    # Get the value of N from the command line arguments
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    # Check the value of N
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    # Create an empty chessboard
    board = [[0 for _ in range(N)] for _ in range(N)]

    # Solve the N-queens problem
    solutions = []
    solve_nqueens(board, 0, solutions)

    # Print the solutions
    print_solutions(solutions)


if __name__ == "__main__":
    main()
