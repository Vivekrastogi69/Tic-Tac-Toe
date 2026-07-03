"""
Tic Tac Toe - GUI Version
Original game logic (NumPy based) kept exactly as the student wrote it.
UI added using Tkinter.
"""

import numpy as np
import tkinter as tk
from tkinter import messagebox

# ---------------------- GAME LOGIC (NumPy - unchanged) ----------------------

board = np.zeros((3, 3), dtype=int)
current = 1  # 1 = X, -1 = O


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


# ---------------------- GUI ----------------------

BG_COLOR = "#1e1e2f"
CELL_COLOR = "#2a2a40"
CELL_HOVER = "#35355a"
X_COLOR = "#4fd1c5"
O_COLOR = "#f687b3"
TEXT_COLOR = "#f5f5f5"

root = tk.Tk()
root.title("Tic Tac Toe")
root.configure(bg=BG_COLOR)
root.resizable(False, False)

score = {"X": 0, "O": 0, "Draw": 0}

title_label = tk.Label(
    root, text="TIC · TAC · TOE", font=("Helvetica", 22, "bold"),
    bg=BG_COLOR, fg=TEXT_COLOR, pady=15
)
title_label.grid(row=0, column=0, columnspan=3)

status_label = tk.Label(
    root, text="Player X's turn", font=("Helvetica", 13),
    bg=BG_COLOR, fg="#a0a0c0"
)
status_label.grid(row=1, column=0, columnspan=3, pady=(0, 10))

buttons = [[None] * 3 for _ in range(3)]


def update_status():
    player = "X" if current == 1 else "O"
    color = X_COLOR if current == 1 else O_COLOR
    status_label.config(text=f"Player {player}'s turn", fg=color)


def reset_board(clear_score=False):
    global board, current
    board = np.zeros((3, 3), dtype=int)
    current = 1
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state="normal", bg=CELL_COLOR)
    if clear_score:
        score["X"] = score["O"] = score["Draw"] = 0
    update_scoreboard()
    update_status()


def update_scoreboard():
    score_label.config(
        text=f"X: {score['X']}     O: {score['O']}     Draws: {score['Draw']}"
    )


def on_click(row, col):
    global current

    if board[row, col] != 0:
        return

    board[row, col] = current
    symbol = "X" if current == 1 else "O"
    color = X_COLOR if current == 1 else O_COLOR
    buttons[row][col].config(text=symbol, fg=color)

    result = check_winner(board)

    if result is not None:
        for i in range(3):
            for j in range(3):
                buttons[i][j].config(state="disabled")
        if result == "Draw":
            score["Draw"] += 1
            status_label.config(text="It's a Draw!", fg="#f6e05e")
            messagebox.showinfo("Game Over", "It's a draw! 🤝")
        else:
            score[result] += 1
            status_label.config(text=f"{result} wins!", fg=(X_COLOR if result == "X" else O_COLOR))
            messagebox.showinfo("Game Over", f"Player {result} wins! 🎉")
        update_scoreboard()
        return

    current = -1 if current == 1 else 1
    update_status()


# Board frame
board_frame = tk.Frame(root, bg=BG_COLOR)
board_frame.grid(row=2, column=0, columnspan=3, padx=20, pady=10)

for i in range(3):
    for j in range(3):
        btn = tk.Button(
            board_frame, text="", font=("Helvetica", 28, "bold"),
            width=4, height=2, bg=CELL_COLOR, fg=TEXT_COLOR,
            activebackground=CELL_HOVER, bd=0, relief="flat",
            command=lambda r=i, c=j: on_click(r, c)
        )
        btn.grid(row=i, column=j, padx=5, pady=5)
        buttons[i][j] = btn

# Scoreboard
score_label = tk.Label(
    root, text="X: 0     O: 0     Draws: 0", font=("Helvetica", 12),
    bg=BG_COLOR, fg="#a0a0c0", pady=10
)
score_label.grid(row=3, column=0, columnspan=3)

# Reset button
reset_btn = tk.Button(
    root, text="New Game", font=("Helvetica", 12, "bold"),
    bg="#4c51bf", fg="white", activebackground="#5a63d8",
    bd=0, relief="flat", padx=15, pady=8,
    command=lambda: reset_board(clear_score=False)
)
reset_btn.grid(row=4, column=0, columnspan=3, pady=(5, 20))

update_status()
root.mainloop()