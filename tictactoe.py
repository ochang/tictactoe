#!/usr/bin/python
# -*- coding: utf-8 -*-

from os import system, name
from random import shuffle, randrange


def clear_screen():
    system("cls") if name == "nt" else system("clear")


def setup_players():
    """
    sets up which game mode (1 play, 2 play, cpu vs cpu) and pieces
    returns a tuple with (str, str, str)
    """

    # first, figure out who has to play
    mode = None
    while mode not in ("1", "2", "c"):
        mode = raw_input("players: [1] human, [2] humans, [c]pu only ").lower()

    # then, figure out who is X and O
    pieces = ["X", "O"]
    shuffle(pieces)

    return (mode, pieces[0], pieces[1])


def print_board(board):
    """Prints an ASCII art representation of a tictactoe grid.
    """
    rows = (range(1,3+1), range(2,6+1), range(7,9+1))

    print "-------------------------------------"
    for row in rows:
        left = board[row[0]] or "_"
        center = board[row[1]] or "_"
        right = board[row[2]] or "_"

        print "|     " + left + \
              "     |     " + center + "     |     " +  \
              right + "     |"
        print "-------------------------------------"


def print_view(board, info, turn):
    namemap = {"2": ("Player 1", "Player 2"),
               "1": ("Player 1", "CPU 1"),
               "c": ("CPU 1", "CPU 2")}
    players = namemap[info[0]]
    print "Move {0} -- {1} is {2}, {3} is {4}".format(
            turn, players[0], info[1], players[1], info[2])

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
    """ if human, we just change value of cell to the player
    elif robot, give to another func
    returns (name of player, piece of player)
    """

    gametype, player1_piece, player2_piece = game_info

    if gametype == "2":
        if (turn % 2 == 1):
            piece = player1_piece
            name = "Player 1"
        else:
            piece = player2_piece
            name = "Player 2"
    # always lets player go first
    elif gametype == "1":
        if (turn % 2 == 1):
            piece = player1_piece
            name = "Player 1"
        else:
            piece = player2_piece
            name = "CPU 1"
            cpu_player(board, player2_piece, turn)
    elif gametype == "c":
        if (turn % 2 == 1):
            piece = player1_piece
            name = "CPU 1"
            cpu_player(board, player1_piece, turn)
        else:
            piece = player2_piece
            name = "CPU 2"
            cpu_player(board, player2_piece, turn)

    if name[0:3] != "CPU":
        while True:
            chosen_cell = raw_input("%s's turn: " % piece)
            if (chosen_cell in board):  # if valid move...
                # assign current player as the value
                # not always guaranteed to work if not an int
                board[int(chosen_cell) - 1] = piece
                if turn != 9:
                    clear_screen()
                break
            else:
                print "invalid input/move. say a coordinate e.g. 0"
                print_board(board)

    return (name, piece)


def cpu_player(board, piece, turn):
    """Change board in place with the move of cpu player
    equivalent to the changes in board made in cell_chooser
    but with logic to choose the best choice
    return None
    """
    # winning combinations
    combos = ((0, 1, 2), (3, 4, 5), (6, 7, 8),  # horizontals
              (0, 3, 6), (1, 4, 7), (2, 5, 8),  # verticals
              (0, 4, 8), (2, 4, 6))             # diagonals
    corners = ["1", "3", "7", "9"]
    shuffle(corners)
    cpu = []
    opponent = []

    for (index, item) in enumerate(board):
        if item == piece:
            cpu.append(index)
        elif item == "O" or item == "X":
            opponent.append(index)

    #print cpu #db
    #print opponent #db
    # detect chance for win
    for combo in combos:
        # if two in what cpu has and two of a winning solution match...
        if (len(set(cpu) & set(combo)) == 2):
            #  and the third one isn't owned by opponent...
            if len((set(combo) - set(cpu)) & set(opponent)) == 0:
                missing = list(set(combo) - set(cpu))[0]
                # print "In an attempt to win... "# db!!!
                print "CPU as %s plays %s" % (piece, board[missing])
                board[missing] = piece
                return None

    # detect chance to block: if opponent has two of a winning combo
    for combo in combos:
        if len(set(opponent) & set(combo)) == 2:
            # gives a list e.g. [6]
            missing = list(set(combo) - set(opponent))[0]
            # print "index of cell opponent is missing = " + str(missing)
            # if I don't own missing already, block
            if missing not in cpu:
                # print "To block..."
                print "CPU as %s plays %s" % (piece, board[missing])
                board[missing] = piece
                return None

    # if turn less than 2 or corners still open...
    if (turn < 2) or (len(set(corners) & set(board)) != 0):
        # pick an untaken corner cell
        missing = list(set(corners) & set(board))[0]
        # print "CPU loves corners and so..."
        print "CPU as %s plays %s" % (piece, board[board.index(missing)])
        board[board.index(missing)] = piece
        return None

    # naive cpu -- chooses a random unasigned square
    # should only happen if no other winning conditions
    else:
        while True:
            rand_cell = board[randrange(0, 9)]
            if (rand_cell != "X") and (rand_cell != "O"):
                # print "In an act of desparation..."
                print "CPU as %s plays %s" % (piece, rand_cell)
                board[board.index(rand_cell)] = piece
                return None


def main():
    # setup
    id_info = ("", "")
    turn = 1
    board = dict.fromkeys(xrange(1,9+1)) 

    clear_screen()
    print "Tic-Tac-Toe Program\n"
    game_info = setup_players()

    # maximum amount of moves in a tictactoe game is 9
    while turn >= 1 and turn <= 9:
        print_view(board, game_info, turn)

        if check_endgame_conditions(board, turn, id_info):
            break

        id_info = cell_chooser(board, game_info, turn)

        turn += 1
    else:
        print "Cat's Game! ^.--.^"

    return 0


if __name__ == "__main__":
    main()
