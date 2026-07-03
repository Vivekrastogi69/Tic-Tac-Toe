"""
Tic Tac Toe - Web Version (Streamlit)
Same NumPy game logic, deployable on the web via Streamlit Community Cloud.
"""

import numpy as np
import streamlit as st

st.set_page_config(page_title="Tic Tac Toe", page_icon="🎮", layout="centered")

# ---------------------- GAME LOGIC (NumPy - unchanged) ----------------------


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


# ---------------------- SESSION STATE ----------------------

if "board" not in st.session_state:
    st.session_state.board = np.zeros((3, 3), dtype=int)
if "current" not in st.session_state:
    st.session_state.current = 1
if "score" not in st.session_state:
    st.session_state.score = {"X": 0, "O": 0, "Draw": 0}
if "winner" not in st.session_state:
    st.session_state.winner = None


def make_move(row, col):
    if st.session_state.winner is not None:
        return
    if st.session_state.board[row, col] != 0:
        return

    st.session_state.board[row, col] = st.session_state.current
    result = check_winner(st.session_state.board)

    if result is not None:
        st.session_state.winner = result
        st.session_state.score[result] += 1
    else:
        st.session_state.current = -1 if st.session_state.current == 1 else 1


def reset_game():
    st.session_state.board = np.zeros((3, 3), dtype=int)
    st.session_state.current = 1
    st.session_state.winner = None


# ---------------------- UI ----------------------

st.markdown(
    "<h1 style='text-align:center;'>🎮 Tic Tac Toe</h1>",
    unsafe_allow_html=True,
)

symbol_map = {0: "", 1: "❌", -1: "⭕"}

# Status message
if st.session_state.winner:
    if st.session_state.winner == "Draw":
        st.markdown("<h3 style='text-align:center;color:#f6e05e;'>It's a Draw! 🤝</h3>", unsafe_allow_html=True)
    else:
        st.markdown(
            f"<h3 style='text-align:center;color:#4fd1c5;'>Player {st.session_state.winner} wins! 🎉</h3>",
            unsafe_allow_html=True,
        )
else:
    player = "X" if st.session_state.current == 1 else "O"
    st.markdown(f"<h4 style='text-align:center;'>Player {player}'s turn</h4>", unsafe_allow_html=True)

# Board
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        with cols[j]:
            st.button(
                symbol_map[st.session_state.board[i, j]] or " ",
                key=f"cell_{i}_{j}",
                on_click=make_move,
                args=(i, j),
                use_container_width=True,
            )

st.divider()

# Scoreboard
c1, c2, c3 = st.columns(3)
c1.metric("Player X", st.session_state.score["X"])
c2.metric("Player O", st.session_state.score["O"])
c3.metric("Draws", st.session_state.score["Draw"])

st.button("🔄 New Game", on_click=reset_game, use_container_width=True)