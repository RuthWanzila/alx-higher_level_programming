#!/usr/bin/python3
"""101-nqueens finds all possible solutions the N queens puzzle, including
translations and reflections.

This program uses virtual backtracking without recursion. In local tests,
the process will
start to slow down visibly for N > 8, and is successful up to N = 11 but
will be killed if used for N > 11. Recursion could allow for a lighter weight
process, but it's not yet apparent how to retain a record of
which solutions are already derived with that method.

Attributes:
    N (int): base no. of queens,also length of board side in piece positions
    candidates (list): list of successful slns for given columns checked

"""
from sys import argv

if len(argv) is not 2:
    print('Usage: nqueens N')
    exit(1)

if not argv[1].isdigit():
    print('N must be a number')
    exit(1)

N = int(argv[1])

if N < 4:
    print('N must be at least 4')
    exit(1)


def board_column_gen(board=[]):
    """Adds a column of zeroes to the right of any board about to be tested for
    queen arrangements in that column.

    Args:
        board (list): A 2D list of integers, only as wide as needed to test
        the rightmost column for queen conflicts.

    Returns:
        list: The modified 2D list.

    """
    if len(board):
        for row in board:
            row.append(0)
    else:
        for row in range(N):
            board.append([0])
    return board


def add_queen(board, row, col):
    """Sets a queen, represented by 1, to the given coordinates in the board.

    Args:
        board (list): A 2D list of integers, only as wide as needed to test
        the rightmost column for queen conflicts.
        row (int): The first dimension index.
        col (int): The second dimension index.

    """
    board[row][col] = 1


def new_queen_safe(board, row, col):
    """Checks if a new queen placed in the rightmost column of the board
    has any conflicts with existing queens.

    Args:
        board (list): 2D list of integers, only as wide as needed
        to test the rightmost column for queen conflicts.
        row (int): The first dimension index.
        col (int): The second dimension index.

    Returns:
        bool: True if no conflicts are found, False otherwise.

    """
    x = row
    y = col

    for i in range(1, N):
        if (y - i) >= 0:
            # Check up-left diagonal
            if (x - i) >= 0:
                if board[x - i][y - i]:
                    return False
            # Check left
            if board[x][y - i]:
                return False
            # Check down-left diagonal
            if (x + i) < N:
                if board[x + i][y - i]:
                    return False
    return True


def coordinate_format(candidates):
    """Converts a board (matrix of 1s and 0s)
    into a list of coordinates for each queen

    Args:
        candidates (list): list of all successful slns for columns last checked

    Returns:
        list: Each member list contains the row and column no. for queen found

    """
    holberton = []
    for x, attempt in enumerate(candidates):
        holberton.append([])
        for i, row in enumerate(attempt):
            holberton[x].append([])
            for j, col in enumerate(row):
                if col:
                    holberton[x][i].append(i)
                    holberton[x][i].append(j)
    return holberton


# Initialize candidates list with the first column of zeros
candidates = []
candidates.append(board_column_gen())

# Proceed column by column, testing the rightmost
for col in range(N):
    # Start a new generation of the candidate list for every round of testing
    new_candidates = []
    # Test each candidate from the previous round at the current column
    for matrix in candidates:
        # For every row in that candidate's rightmost column
        for row in range(N):
            # Check if any conflicts in placing a queen at those coordinates
            if new_queen_safe(matrix, row, col):
                # Create a "child" (copy) of that candidate
                temp = [line[:] for line in matrix]
                # Place a queen in that position
                add_queen(temp, row, col)
                # Add a new column of zeros on the right for the next round
                if col < N - 1:
                    board_column_gen(temp)
                # Add the new candidate to this round's list of successes
                new_candidates.append(temp)
    # Discard the "parent" candidates when finished with the round
    candidates = new_candidates

# Format results to match the assignment output
for item in coordinate_format(candidates):
    print(item)
