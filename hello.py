import numpy as np


board = np.zeros((3, 3), dtype=int)
# for printing the board
def print_board(b):
    symbol = {0: " ", 1: "X", -1: "O"}
    for i in range(3):
        row = "|".join(symbol[val] for val in b[i])
        print(" "+ row)
        if i < 2:
            print("---+---+---")
    print()

print_board(board)

def check_winner(b):
    if 3 in np.sum(b, axis=1) or 3 in np.sum(b, axis=0):
        return "X"

    if -3 in np.sum(b, axis=1) or -3 in np.sum(b, axis=0):
        return "O"

    if np.trace(b) == 3 or np.trace(np.fliplr(b)) == 3:
        return "X"

    if np.trace(b) == -3 or np.trace(np.fliplr(b)) == -3:
        return "O"

    if 0 not in b:
        return "Draw"

    return None

current = 1

print("Welcome to Tic Tac Toe!")

while True:
    if current == 1:
        player = "X"
    else:
        player = "O"

    try:
        row = int(input(player + " enter row (0,1,2): "))
        column = int(input(player + " enter column (0,1,2): "))
    except ValueError:
        print("please enter number only \n")
        continue

    if row  < 0 or row > 2 or column < 0 or column > 2:
        print("please enter valid row and column \n")
        continue
        
    if board[row,column] != 0:
        print("cell is already taken ")
        continue

    board[row,column] = current
    print_board(board)

    result = check_winner(board)

    if result is not None:
        if result == "Draw":
            print("ohhh! its a draw")
        else:
            print(result + " wins the game")
        break
        
    if current == 1:
        current = -1
    else:
        current = 1