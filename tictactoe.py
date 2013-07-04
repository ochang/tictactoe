#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import system, name
from random import shuffle

from cpu_player import choose_piece


NAME_MAP = {"2": ("Player 1", "Player 2"),
            "1": ("Player 1", "CPU 1"),
            "c": ("CPU 1", "CPU 2")}
WINNING_COMBOS = ((1, 2, 3), (4, 5, 6), (7, 8, 9),  # horizontals
                  (1, 4, 7), (2, 5, 8), (3, 6, 9),  # verticals
                  (1, 5, 9), (3, 5, 7))             # diagonals


def clear_screen():
    system("cls") if name == "nt" else system("clear")


def setup_players():
    """
    sets up which game mode (1 play, 2 play, cpu vs cpu) and pieces
    returns a tuple with (str, str, str)
    """
    mode = None
    while mode not in ("1", "2", "c"):
        mode = raw_input("players: [1] human, [2] humans, [c]pu only ").lower()

    # figure out who is X and O
    pieces = ["X", "O"]
    shuffle(pieces)

    return (mode, pieces[0], pieces[1])


def print_board(board):
    """Prints an ASCII art representation of a tictactoe grid.
    """
    rows = (range(1, 3+1), range(4, 6+1), range(7, 9+1))

    print "-------------------------------------"
    for row in rows:
        left = board[row[0]] or str(row[0])
        center = board[row[1]] or str(row[1])
        right = board[row[2]] or str(row[2])

        print "|     {0}     |     {1}     |     {2}     |".format(
            left, center, right)
        print "-------------------------------------"


def print_view(board, info, turn):
    # Status line
    players = NAME_MAP[info[0]]
    print "Move {0} -- {1} is {2}, {3} is {4}".format(
          turn, players[0], info[1], players[1], info[2])

    # Board
    print_board(board)


def check_endgame_conditions(board, turn):
    """Takes list of board, int turn, list of last name and piece. Returns...
        -- True if there is a winner
        -- False if there is still potential winner
        -- Ends script if there can be no winner
    """
    # have to play 5 rounds before a winner can occur
    if turn <= 5:
        return (False, None)

    # winning combinations
    x_owns = set([index for index in board if board[index] == "X"])
    o_owns = set([index for index in board if board[index] == "O"])

    # test for winning-ness
    for winning_combo in WINNING_COMBOS:
        winning_combo = set(winning_combo)
        if winning_combo.issubset(x_owns) or winning_combo.issubset(o_owns):
            return (True, winning_combo)

    # test for catiness/scratchiness
    possible_winning_combos = 0
    for combo in WINNING_COMBOS:
        # each cell can only be owned by one player
        # find the number of cells that each player owns in this combo
        o_cells = len(x_owns & set(combo))
        x_cells = len(o_owns & set(combo))

        # if all the combos cells are not taken by different players and
        # it is still possible for a player to get all the cells of combo
        if (o_cells + x_cells != 3) and not (o_cells == 1 and x_cells == 1):
            possible_winning_combos += 1

    return (None if possible_winning_combos == 0 else False), None


def cell_chooser(board, info, turn):
    """Develop a prompt for current user and prompt them to pick a valid board
    index. Returns a tuple with the piece (X or O) and the index chosen.
    """
    gametype, player1_piece, player2_piece = info
    player1, player2 = NAME_MAP[gametype]

    if turn % 2 == 1:
        name = player1
        piece = player1_piece
    else:
        name = player2
        piece = player2_piece

    if name[0:3] == "CPU":
        return choose_piece(board, turn, piece)
    else:
        while True:
            try:
                chosen_cell = int(raw_input("{0}'s turn: ".format(piece)))
            except ValueError:
                pass

            if (chosen_cell in board) and (board[chosen_cell] is None):
                return (piece, chosen_cell)
            else:
                print "invalid input/move. say a coordinate e.g. 0"


def main():
    turn = 0
    player = None
    board = dict.fromkeys(xrange(1, 9+1))

    clear_screen()
    print "Tic-Tac-Toe Program\n"
    game_info = setup_players()

    # maximum amount of moves in a tictactoe game is 9
    while turn <= 9:
        print_view(board, game_info, turn)

        # Check endgame conditions and break if necessary
        winner_exists, combo = check_endgame_conditions(board, turn)
        if winner_exists:
            print "{0} wins with combo {1}!".format(player, tuple(combo))
            break
        elif winner_exists is None:
            print "No more winning solutions. :("
            break

        # Pick a piece, either CPU or player
        (player, cell) = cell_chooser(board, game_info, turn)
        # Update the board
        board[cell] = player

        turn += 1
    else:
        print "Cat's Game! ^.--.^"

    return 0


if __name__ == "__main__":
    main()
