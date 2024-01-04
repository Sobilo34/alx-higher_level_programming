#!/usr/bin/python3
"""
This module defines a Rectangle class with private width & height attributes.
"""
import sys


def init_board(n):
    """
    Initialize the chessboard with empty spaces.

    Args:
        n (int): Size of the chessboard.

    Returns:
        list: Initialized chessboard represented as a list of lists.
    """
    bd = []  # bd -> board
    [bd.append([]) for i in range(n)]
    [row.append(' ') for i in range(n) for row in bd]
    return bd


def board_deepcopy(board):
    """
    Perform a deep copy of the given chessboard.

    Args:
        board (list): Chessboard represented as a list of lists.

    Returns:
        list: Deep copy of the input chessboard.
    """
    if isinstance(board, list):
        return list(map(board_deepcopy, board))
    return board


def get_solution(board):
    """
    Get the positions of the queens on the chessboard.

    Args:
        board (list): Chessboard represented as a list of lists.

    Returns:
        list: List of positions of queens on the chessboard.
    """
    soln = []  # soln -> solution
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                soln.append([r, c])
                break
    return soln


def xout(board, row, col):
    """
    Mark the attacked positions by a queen with 'x'.

    Args:
        board (list): Chessboard represented as a list of lists.
        row (int): Row index of the queen.
        col (int): Column index of the queen.

    Modifies:
        Modifies the input board by marking attacked positions with 'x'.
    """
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c]
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """
    Recursively solve the N-Queens problem using backtracking.

    Args:
        board (list): Chessboard represented as a list of lists.
        row (int): Current row being considered.
        queens (int): Number of queens placed on the board.
        solutions (list): List to store the solutions.

    Returns:
        list: List of solutions for the N-Queens problem.
    """
    solns = solutions  # soln -> solutions
    if queens == len(board):
        solns.append(get_solution(board))
        return solns

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_board = board_deepcopy(board)
            tmp_board[row][c] = "Q"
            xout(tmp_board, row, c)
            solns = recursive_solve(tmp_board, row + 1,
                                    queens + 1, solns)

    return solns


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = init_board(int(sys.argv[1]))
    solns = recursive_solve(board, 0, 0, [])  # solns -> solutions
    for sol in solns:
        print(sol)
