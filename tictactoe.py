#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import system, name
from random import shuffle

# from cpu_player import cpu_strategy


NAME_MAP = {"2": ("Player 1", "Player 2"),
            "1": ("Player 1", "CPU 1"),
            "c": ("CPU 1", "CPU 2")}


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
    rows = (range(1, 3+1), range(2, 6+1), range(7, 9+1))

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


def check_endgame_conditions(board, turn, names):
    """Takes list of board, int turn, list of last name and piece. Returns...
        -- True if there is a winner
        -- False if there is still potential winner
        -- Ends script if there can be no winner
    """

    # have to play 5 rounds before a winner can occur
    if turn <= 5:
        return False

    # winning combinations
    combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontals
              (0, 3, 6), (1, 4, 7), (2, 5, 8),  # verticals
              (0, 4, 8), (2, 4, 6))             # diagonals
    possible_winning_combos = 0
    piece = names[1]
    x_list = []
    o_list = []

    for (index, item) in enumerate(board):
        if item == "X":
            x_list.append(index)
        elif item == "O":
            o_list.append(index)

    # test for winning-ness
    for combo in combos:
        for list_ in (x_list, o_list):
            # from http://stackoverflow.com/questions/1388818/
            # how-can-i-compare-two-lists-in-python-and-return-matches
            if len(set(list_) & set(combo)) == 3:
                if list_ == x_list:
                    print names[0] + " as " + names[1] + " wins!"
                    return True
                elif list_ == o_list:
                    print names[0] + " as " + names[1] + " wins!"
                    return True

    # test for catiness/scratchiness
    for combo in combos:
        # each cell can only be owned by one person, allows us to say
        # how many of the cells in combo o owns
        o_owns = len(set(x_list) & set(combo))
        # how many of the cells in combo x owns
        x_owns = len(set(o_list) & set(combo))

        # print combo, o_owns, x_owns # db!!! looks kind of cool

        # if nobody owns all of that combo, move on
        if ((o_owns + x_owns) == 3) or ((o_owns == 1) and (x_owns == 1)):
            # combo can't be won off of
            pass
        elif (turn > 8) and (o_owns == 2) and (piece == "X"):
            pass
        elif (turn > 8) and (x_owns == 2) and (piece == "O"):
            pass
        else:
            possible_winning_combos += 1

    if possible_winning_combos == 0:
        print "Cat's game! Everyone's a loser!"
        raise SystemExit(0)

    return False


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
        return cpu_strategy(board, turn)
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
    turn = 1
    board = dict.fromkeys(xrange(1, 9+1))

    clear_screen()
    print "Tic-Tac-Toe Program\n"
    game_info = setup_players()

    # maximum amount of moves in a tictactoe game is 9
    while turn >= 1 and turn <= 9:
        print_view(board, game_info, turn)
        if check_endgame_conditions(board, turn, id_info):
            break

        (player, cell) = cell_chooser(board, game_info, turn)
        # Update the board
        board[cell] = player

        turn += 1
    else:
        print "Cat's Game! ^.--.^"

    return 0


if __name__ == "__main__":
    main()
