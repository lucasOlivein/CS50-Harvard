
# #️⃣ Tic-Tac-Toe
>Using Minimax, implement an AI to play Tic-Tac-Toe optimally.
## 🚀 Summary

This project implements an **unbeatable Tic-Tac-Toe AI** using the **Minimax algorithm**, ensuring optimal decision-making in every possible game state.

The game is modeled as a search problem where each board configuration represents a state, and players alternate turns until a terminal state (win, loss, or draw) is reached. The AI recursively evaluates possible moves to select actions that maximize its own outcome while minimizing the opponent’s.

The implementation emphasizes:

- Clean functional design
- Immutable board state transitions
- Deterministic game evaluation
- Separation between game logic and user interface

Each core function was implemented and committed independently to preserve traceability and document the development process at a fine-grained level.


## 📄  Official Description (Adapted)
This project consists of two main files: `runner.py` and `tictactoe.py`.

- ### 🖥️  The Graphical Interface: `runner.py`   
    This file is provided fully implemented. It handles the graphical interface that allows the game to be visually played. Once the logic in `tictactoe.py` is complete, it can be run with:
    ```bash
    python runner.py
    ```

- ### 🧠  Game Logic: `tictactoe.py`
    This file contains all the core logic of the game, including move validation, turn handling, game state evaluation, and optimal move selection. Most of the functions in this file was *left to be implemented*.

### 🛠️  Initial Setup
- ### 🔢  Constants

    At the top of `tictactoe.py`, three constants are defined:

    - `X`: represents player X
    - `O`: represents player O
    - `EMPTY`: represents an empty cell on the board

    These values represent the state of each cell.

- ### 🧩  Board Representation
    The board is represented as a list of three lists (i.e., a 3x3 grid).  
Each inner list corresponds to a row on the board and contains three values: `X`, `O`, or `EMPTY`.

    For example:
    ```python
    [
        [X, O, EMPTY],
        [EMPTY, X, EMPTY],
        [O, EMPTY, X]
    ]
    ```
    The `initial_state` function returns the starting state of the board: a 3x3 grid where all cells are `EMPTY`.

### ⚙️  Specification
The following functions in `tictactoe.py` was left to be implemented:

#### 📌  `player(board)`
- ✅  Return which player’s turn it is (either `X` or `O`) on the `board`.
- ✅  If `board` is **initial board**, `X` gets the first move. 
- ✅  Players alternate with each additional move.
- ✅  If `board` is a **terminal board**, then any return value is acceptable (i.e., the game is already over).


#### 📌  `actions(board)`
- ✅  Return a set of all of the possible actions (moves) that can be taken on `board`.
- ✅  Each action should be represented as a tuple (i, j), where:
    - `i` corresponds to the row of the move (0, 1, or 2)
    - `j` corresponds to which cell in the row corresponds to the move (0, 1, or 2)
- ✅  Only cells with `EMPTY` are valid moves.
- ✅  If it's a **terminal board**, then any return value is acceptable.


#### 📌  `result(board, action)`
- ✅  Should return a **new board** without modifying the *input* `board`.
    - The *new board* should be the *input* `board` assigned with the current player (`X` or `O`) in the `action` coordinate.
- ✅  If `action` is not a valid move for the *input* `board`, it should `raise` an `exception`.


#### 📌  [`winner(board)`](https://github.com/lucasOlivein/CS50-Harvard/commit/df75a6ff1b7f518faf2c673b1e4fec2ceae5b56d)
- ✅  Return the winner (`X` or `O`) of the `board` if there is one, or `None` otherwise.
- ✅  One can win the game with three of their moves in a row horizontally, vertically, or diagonally.


#### 📌  `terminal(board)`
- ✅  Return `True` if the game is over, or `False` otherwise.


#### 📌  `utility(board)`
- ✅  Accept the **terminal board** `board` and returns its utility:
    - `1` if `X` has won the game,
    - `-1` if `O` has won the game,
    - `0` if the game has ended in a tie.

#### 📌  [`minimax(board)`](https://github.com/lucasOlivein/CS50-Harvard/commit/c4aa6f471c4f45c3bee67ccddb8e2cb728df1ca8)
- ✅  Return the optimal move for the player to move on the `board`.
- ✅  The move returned should be the optimal action (i, j) that is one of the allowable actions on the `board`. 
- ✅  If multiple moves are equally optimal, any of those moves is acceptable.
- ✅  If `board` is a **terminal board**, the `minimax` function should return `None`.

### 🧱 Assumptions
- `utility` function is only called on a `board` if the return of `terminal(board)` is `True`.
- There will be at most one winner (no simultaneous wins).
- For all functions that accept a `board` as input, the `board` is a **valid board**.
    - A *valid board* is a list that contains three rows, each with three values of either `X`, `O`, or `EMPTY`.


### 🔒 Constraints
- ✅  `result(board)` should not modify the *input* `board`:  
    Since Minimax ultimately requires considering many **different board** states during its computation, simply updating a cell in the *input* `board` is not a correct implementation of the `result` function. 

- ✅  The **functions declarations** provided should not be modified (the order or number of arguments to each function).

###  🏁 Running the Game
Once all functions are implemented correctly, it can be run:
```python
    python runner.py
``` 
You will be able to play against an AI opponent. And, since Tic-Tac-Toe is a tie given optimal play by both sides, you should never be able to beat the AI (though if you don’t play optimally as well, it may beat you!)

### 💡 Hints Provided
- ✅ You're likely to make a [deep copy](https://docs.python.org/3/library/copy.html#copy.deepcopy) of the `board` in the [`result`](https://github.com/lucasOlivein/CS50-Harvard/commit/30ffd4da15da71fcc1735dab11fefd9918d2e2ca) function.
- To test individual functions, you can import in a different Python file:
```python
from tictactoe import initial_state, player, ...
```
- ✅ You’re welcome to add additional helper functions to `tictactoe.py`, provided that their names do not collide with function or variable names already in the module.

- **Alpha-beta pruning** is optional, but may make the AI run more efficiently!

### 🎯  Solution
| Feature | Commit |
|----------|--------|
|`minimax`| [c4aa6f4](https://github.com/lucasOlivein/CS50-Harvard/commit/c4aa6f471c4f45c3bee67ccddb8e2cb728df1ca8)
|`utility`| [697744a](https://github.com/lucasOlivein/CS50-Harvard/commit/697744aa1e8959cba66fd3c476ffd271f26025ed)
|`winner` | [df75a6f](https://github.com/lucasOlivein/CS50-Harvard/commit/df75a6ff1b7f518faf2c673b1e4fec2ceae5b56d)
| `result`| [30ffd4d](https://github.com/lucasOlivein/CS50-Harvard/commit/30ffd4da15da71fcc1735dab11fefd9918d2e2ca)
| `terminal`| [ee0dbad](https://github.com/lucasOlivein/CS50-Harvard/commit/ee0dbad862bc0916d45dffa1f6cea04be600fe25)
| `player` | [9ace8e4](https://github.com/lucasOlivein/CS50-Harvard/commit/9ace8e4bccc906068c694b8f00683b0ca354879b)
| `actions` | [2e827a3](https://github.com/lucasOlivein/CS50-Harvard/commit/2e827a3f557e88a2d30a329cc81bab7aa92b279b)

### 📚  Source
Based on *Tic-Tac-Toe* project from the Harvard AI course, available at: [https://cs50.harvard.edu/ai/2024/projects/0/tictactoe](https://cs50.harvard.edu/ai/2024/projects/0/tictactoe/).