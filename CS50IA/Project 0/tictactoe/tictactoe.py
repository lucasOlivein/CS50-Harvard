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
    winner = None
    # Vertical check
    for col, _ in enumerate(board):  # Keep the column fixed and vary the row.
        for row, _ in enumerate(board):
            # The board is a list of rows, each row is a list of cells.
            # So, board[i][j] refers to the cell at row i and column j.
            if board[row][col] == EMPTY:
                break
            # At the first iteration of each column, set the potential winner.
            # If the same value persists through all rows in the column, return the winner.
            if row == 0:
                winner = board[row][col]
            else: 
                if board[row][col] != winner: 
                    winner = None
                    break
                elif row == 2:
                    return winner

    # Horizontal check
    for row, _ in enumerate(board):  # Keep the row fixed and vary the colum.
        for col, _ in enumerate(board):
            if board[row][col] == EMPTY:
                break
            # At the first iteration of each row, set the potential winner.
            # If the same value persists through all columns in the row, return the winner.
            if col == 0:
                winner = board[row][col]
            else:
                if board[row][col] != winner:
                    winner = None
                    break
                elif col == 2:
                    return winner

    # Main Diagonal check
    for main_diag, _ in enumerate(board):
        if board[main_diag][main_diag] == EMPTY:
            break
        # Same logic as used in the previous checks, but applied to the main diagonal (top-left to bottom-right).
        # If the same value persists through the diagonal, return the winner.
        if main_diag == 0:
            winner = board[main_diag][main_diag]
        else:
            if board[main_diag][main_diag] != winner:
                winner = None
                break
            elif main_diag == 2:
                return winner
    
    # Secondary Diagonal check
    for sec_diag, _ in enumerate(board):
        if board[sec_diag][2 - sec_diag] == EMPTY:
            break
        # Same logic as used in the previous checks, but aplied to the secondary diagonal (top-right to bottom-left).
        # If the same value persists, return the winner.
        if sec_diag == 0:
            winner = board[sec_diag][2 - sec_diag]
        else:
            if board[sec_diag][2 - sec_diag] != winner:
                winner = None
                break
            elif sec_diag == 2:
                return winner
    
    return None


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
    winning_player = winner(board)

    if winning_player == X:
        return 1
    elif winning_player == O:
        return -1
    else:
        return 0
    

def minimax(board):
    # Alpha-beta pruning not implemented, since I plan to play perfectly.
    # The AI should never beat me anyway.
    """
    Returns the optimal action for the current player on the board.
    """
    # This recursive function explores all possible game states.
    def evaluate(board):
        if terminal(board):
            return utility(board)

        res = []
        # Recursively simulate all future board states.
        # Apply each possible action to a copy of the current board in the recursive calls.
        for action in actions(board):
            board_result = result(board, action)
            res.append(evaluate(board_result))
        
        # It returns the optimal result for the current player. 
        if player(board) == X:
            return max(res)
        else:
            return min(res)
    
    # Start the Minimax
    if terminal(board):
        return None
    
    results = []
    action = list(actions(board))

    # Evaluate all possible actions.
    # The `results` list mirrors the `action` list —  
    # the index of a result corresponds to the index of the action that produced it.
    for act in action:
        board_result = result(board, act)
        results.append(evaluate(board_result))

    # Select the optimal result based on the current player.
    if player(board) == X:
        optimal = max(results)
    else:
        optimal = min(results)

    # Search for the action that produced the optimal result.
    for i, act in enumerate(action):
        if optimal == results[i]:
            return act
