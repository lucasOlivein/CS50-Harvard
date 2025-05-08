"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count_X = 0
    count_O = 0

    # The board is a list of rows. 
    # Each row is a list of columns (cells).
    for rolls in board:
        for cell in rolls:
            if cell == X:
                count_X += 1
            elif cell == O:
                count_O += 1

    if count_X == count_O:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    # i is the row index, and j is the column index. 
    # (i, j) represents a possible action.
    for i, rows in enumerate(board):
        for j, cell in enumerate(rows):
            # # A cell with value EMPTY indicates a valid action.
            if cell == EMPTY:
                actions.add((i, j))
    
    return actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    # Check if the action is valid.
    # Ensure action is within board limits and targets an EMPTY cell.
    if 0 <= i <= 2 and 0 <= j <= 2:
        if board[i][j] == EMPTY:
            result = copy.deepcopy(board)
            result[i][j] = player(board)
            return result
        
    raise Exception


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board):
        return True
    
    # If there is at least one empty cell, then it is not a terminal board.
    for row in board: 
        for cell in row:
            if cell == EMPTY:
                return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
