# 🎮 Tic Tac Toe (Python + NumPy)

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://tic-tac-toe-b9f6qh2pjszwnjcr8chvz3.streamlit.app/)

**🔗 Live Demo:** [tic-tac-toe-b9f6qh2pjszwnjcr8chvz3.streamlit.app](https://tic-tac-toe-b9f6qh2pjszwnjcr8chvz3.streamlit.app/)

A classic Tic Tac Toe game built in Python, using **NumPy** for the game logic and **Tkinter** for a clean, modern graphical interface. Also deployed as a web app using **Streamlit**.

---

## 📌 About the Project

This project started as a simple console-based Tic Tac Toe game where the board and win-checking logic were handled entirely using NumPy arrays. It has since been upgraded with a graphical interface, making it easy and fun to play by simply clicking on the board.

---

## ✨ Features

- 🎨 Clean, dark-themed graphical interface (Tkinter)
- 🧮 Game logic powered by **NumPy** (rows, columns, and diagonals checked using array operations)
- 🖱️ Click-to-play — no manual row/column typing needed
- 🏆 Live scoreboard (tracks wins for X, O, and draws)
- 🔁 "New Game" button to restart instantly without closing the app
- ✅ Draw detection and winner popup messages

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| NumPy | Board representation & win-checking logic |
| Tkinter | Graphical User Interface (GUI) |

---

## 📂 Project Structure

```
tic-tac-toe/
│
├── app.py                # Web version (Streamlit) - deployed live
├── tic_tac_toe_gui.py    # Desktop version (Tkinter)
├── requirements.txt      # Dependencies for deployment
└── README.md             # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone or Download

Download the project files or copy `tic_tac_toe_gui.py` to a folder on your computer.

### 2. Install Requirements

Make sure Python is installed. Then install NumPy:

```bash
pip install numpy
```

> **Note:** Tkinter comes pre-installed with Python. If it's missing (rare, mostly on Linux), install it with:
> ```bash
> sudo apt-get install python3-tk
> ```

### 3. Run the Game

**Desktop version (Tkinter):**
```bash
python tic_tac_toe_gui.py
```
The game window will open automatically. 🎉

**Web version (Streamlit) — run locally:**
```bash
pip install streamlit
streamlit run app.py
```
Or simply try it live without installing anything: [🔗 Live Demo](https://tic-tac-toe-b9f6qh2pjszwnjcr8chvz3.streamlit.app/)

---

## 🕹️ How to Play

1. Player **X** goes first, followed by Player **O**.
2. Click on any empty cell on the 3x3 grid to place your mark.
3. The first player to get 3 marks in a row (horizontally, vertically, or diagonally) wins.
4. If all 9 cells are filled with no winner, the game ends in a **Draw**.
5. Click **"New Game"** to play again — your score is saved until you restart the app.

---

## 🧠 How the Logic Works (NumPy)

The board is represented as a 3x3 NumPy array:
- `0` → empty cell
- `1` → Player X
- `-1` → Player O

Winner detection uses simple array math:
- **Rows/Columns:** Sum of a row or column equals `3` (X wins) or `-3` (O wins)
- **Diagonals:** `np.trace()` checks the main diagonal, `np.trace(np.fliplr(board))` checks the anti-diagonal
- **Draw:** If no `0` remains in the board and no winner is found

---

## 🚀 Future Improvements

- 🤖 Add an AI opponent (Minimax algorithm) for single-player mode
- 🔊 Add sound effects for moves and win/draw events
- 🌐 Build a web version using Streamlit
- 📊 Add a data-tracking feature to log game history

---

## 👤 Author

Made by a Data Science student as a Python + NumPy practice project.

---

## 📄 License

This project is free to use for learning and personal projects.