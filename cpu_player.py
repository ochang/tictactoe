#!/usr/bin/python
# -*- coding: utf-8 -*-

from random import sample

WINNING_COMBOS = ((1, 2, 3), (4, 5, 6), (7, 8, 9),  # horizontals
                  (1, 4, 7), (2, 5, 8), (3, 6, 9),  # verticals
                  (1, 5, 9), (3, 5, 7))             # diagonals


def choose_piece(board, turn, piece):
    """Logic CPU uses to determine strategy.
    Returns (piece, cell_index)
    """
    cpu = set([index for index in board if board[index] == piece])
    opponent_piece = "X" if piece == "O" else "O"
    opponent = set([index for index in board if board[index] == opponent_piece])

    # detect chance for win
    for combo in WINNING_COMBOS:
        # if two in what cpu has and two of a winning solution match...
        combo = set(combo)
        if len(cpu & combo) == 2:
            # and the third one isn't owned by opponent...
            if len((combo - cpu) & opponent) == 0:
                missing = (combo - cpu).pop()
                return (piece, missing)

    # detect chance to block: if opponent has two of a winning combo
    for combo in WINNING_COMBOS:
        combo = set(combo)
        if len(opponent & combo) == 2:
            missing = (combo - opponent).pop()
            # if I don't own missing already, block
            if missing not in cpu:
                return (piece, missing)

    corners = set(["1", "3", "7", "9"])
    untaken_corners = corners - cpu - opponent
    # if turn less than 2 or corners still open...
    if turn < 2 or len(untaken_corners) != 0:
        # pick an untaken corner cell
        random_corner = sample(untaken_corners, 1)[0]
        return (piece, random_corner)

    # naive cpu -- chooses a random unassigned square
    # should only happen if no other winning conditions
    untaken_cells = set(board) - cpu - opponent
    random_cell = sample(untaken_cells, 1)[0]
    return (piece, random_cell)
