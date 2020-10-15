
import numpy as np

"""
Example 1:

Input: moves = [[0,0],[2,0],[1,1],[2,1],[2,2]]
Output: "A"
Explanation: "A" wins, he always plays first.
"X  "    "X  "    "X  "    "X  "    "X  "
"   " -> "   " -> " X " -> " X " -> " X "
"   "    "O  "    "O  "    "OO "    "OOX"

Example 2:

Input: moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
Output: "B"
Explanation: "B" wins.
"X  "    "X  "    "XX "    "XXO"    "XXO"    "XXO"
"   " -> " O " -> " O " -> " O " -> "XO " -> "XO " 
"   "    "   "    "   "    "   "    "   "    "O  "

Example 3:

Input: moves = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]
Output: "Draw"
Explanation: The game ends in a draw since there are no moves to make.
"XXO"
"OOX"
"XOX"

Example 4:

Input: moves = [[0,0],[1,1]]
Output: "Pending"
Explanation: The game has not finished yet.
"X  "
" O "
"   "
"""
moves1 = [[0,0],[2,0],[1,1],[2,1],[2,2]]
moves2 = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
moves3 = [[0,0],[1,1]]
moves4 = [[0,0],[1,1],[2,0],[1,0],[1,2],[2,1],[0,1],[0,2],[2,2]]

def get_state(moves, size):
    # Split the moves into two sets? Lose some information, but simplify problem. Can we retain O(k)? yes.
    # Only way to return pending is if we get to end of moves and nobody has won.
    a_moves = moves[::2]
    b_moves = moves[1::2]
    if len(moves) == size**2:
        return "draw"
    elif _get_state(a_moves, size):
        return "A"
    elif _get_state(b_moves, size):
        return "B"
    else:
        return "pending"
    
def _get_state(moves, size):
    rows = {}
    columns = {}
    diagonals = {'main': 0, 'rotated': 0}
    
    for move in moves:
        row, column = move
        if row in rows:
            rows[row] += 1
        else:
            rows[row] = 1
            
        if column in columns:
            columns[column] += 1
        else:
            columns[column] = 1
            
        if row == column:
            diagonals['main'] += 1
        if size - row - 1 == column:
            diagonals['rotated'] += 1
        if (size in rows.values() or size in columns.values() or size in diagonals.values()):
            return True
    return False
        


# Other version:



test1 = np.array([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]])
   

test2 = np.array([
    [1, 0, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0]])


test3 = np.array([
    [0, 0],
    [0, 0]])

test4 = np.array([
    [0, 1],
    [1, 0]])

test5 = np.array([
    [1, 0],
    [0, 1]])

test6 = np.array([
    [1, 0, 1, 1, 0],
    [1, 1, 1, 1, 1],
    [0, 1, 1, 0, 0],
    [0, 1, 1, 1, 0],
    [1, 0, 0, 0, 1]])


def test():
    arguments = [test1, test2, test3, test4, test5, test6]
    
    def test_cases(function, args, results):
        for arg, result in zip(arguments, results):
            assert function(arg) == result
    
    def test_check_horizontal():
        results = [False, False, False, False, False, True]
        test_cases(check_horizontal, arguments, results)
    
    def test_check_vertical():
        results = [False, False, False, False, False, False]
        test_cases(check_vertical, arguments, results)
    
    def test_check_diagonal():
        results = [False, False, False, True, True, True]
        test_cases(check_diagonal, arguments, results)
            
    def test_check_board():
        results = [False, False, False, True, True, True]
        test_cases(check_board, arguments, results)
    
    test_check_vertical()
    test_check_horizontal()
    test_check_diagonal()
    test_check_board()
    

def check_board(board):
    return check_vertical(board) or check_horizontal(board) or check_diagonal(board)

def check_vertical(board):
    board_size = board.shape[0]
    return np.any(np.sum(board, axis=0) == board_size)

def check_horizontal(board):
    board_size = board.shape[0]
    return np.any(np.sum(board, axis=1) == board_size)

def check_diagonal(board):
    board_size = board.shape[0]
    return np.trace(board) == board_size or np.trace(np.rot90(board)) == board_size

def check_if_negatives_won(board):
    return check_board(-1 * board)



