from os import system, name
from random import shuffle, randrange

def clear_screen():
    """ 
    support for clearing screens on multi-platforms
    http://stackoverflow.com/questions/517970/how-to-clear-python-interpreter-console
    """
    if name == "nt":
        system("cls")
    else:
        system("clear")

def print_board(board):
    """ 
    Prints an ASCII art representation of a tictactoe grid. Assumed that 'board' is given in a list fomat that goes down the first row's colums and then proceeds to second row i.e. [first row cells, second row cells, third row cells]. 
    """
    i = 0
    print "-------------------------------------"
    for x in range(3): # for every row...
        for x in range(3): # for every column (left, center, right)...
            # the zero at the end is so we only take one char
            # avoids issues with printing board with whitespace
            if i in (0, 3, 6):
                left = board[i][0]
            elif i in (1, 4, 7):
                center = board[i][0]
            elif i in (2, 5, 8):
                right = board[i][0]
            else:
                print "unexpected index"
            i += 1 # incerement so next pass is for the next cell
        
        print "|     " + left + "     |     " + center + "     |     " + right + "     |"
        print "-------------------------------------"

def print_view(info, board, turn):
    # print top status bar
    if info[0] == "2": # two humans
        print "Move #%i -- Player 1 is %s, Player 2 is %s" % (turn, info[1], info[2])
    elif info[0] == "1": # one human, one CPU; computer is always second
        print "Move #%i -- Player 1 is %s, CPU 1 is %s" % (turn, info[1], info[2])
    elif info[0] == "c":
        print "Move #%i -- CPU 1 is %s, CPU 2 is %s" % (turn, info[1], info[2])

    print_board(board)
                
def check_win(board, turn, names):
    """ 
    Given list ownership which is comprised of position strings and ownership strings ('X' and 'O'), outputs winning piece if there is a winner. 
    Return true(winner) or false
    """
    # winning combinations -- refer to cells by their indices
    combos = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
    xs = []
    os = []
    # have to play 5 rounds before a winner can occur
    if turn <= 5:
        return False
  
    # generate list of who owns which square
    for (index, item) in enumerate(board):
        if item == "X":
            xs.append(index)
        elif item == "O":
            os.append(index)

    players = (xs, os)
    for combo in combos:
        for player in players:
            # from http://stackoverflow.com/questions/1388818/how-can-i-compare-two-lists-in-python-and-return-matches
            if len(set(player) & set(combo)) == 3: 
                if player == xs:
                    print names[0] + " as " + names[1] + " wins!"
                    return True
                elif player == os:
                    print names[0] + " as " + names[1] + " wins!"
                    return True
                
def cell_chooser(info, board, turn):
    """
    if human, this is easy; we just change value of cell to the player
    elif robot, give to another func
    returns nothing
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
            if (chosen_cell in board): # if valid move...
                # assign current player as the value
                # not always guaranteed to work if not an int
                board[int(chosen_cell) - 1] = piece
                clear_screen()
                break
            else:
                print "invalid input/move. say a coordinate e.g. 0"
                print_board(board)

    return (name, piece)

def cpu_player(board, piece, turn):
    """
    change board in place with the move of cpu player
    equivalent to the changes in board made in cell_chooser
    but with logic to choose the best choice
    return None
    """
    # winning combinations
    combos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
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
    
    moved = False
    
    # detect chance for win
    for combo in combos:
        # if two in what cpu has and two of a winning solution match...
        if (len(set(cpu) & set(combo)) == 2):
            #  and the third one isn't owned by opponent...
            if len((set(combo) - set(cpu)) & set(opponent)) == 0:    
                missing = list(set(combo) - set(cpu))[0]
                print "In an attempt to win... "# db!!!
                print "CPU as %s plays %s" % (piece, board[missing])
                board[missing] = piece
                return None
    # vvvvv don't really understand why this is vvvvv
    # need to be in 2 for loops or else it will stop when it has the chance to win. if there is the chance to win and the chance to block, it possibly will take the block. this ensures that all the combos are used before going for a block

    # detect chance to block: if opponent has two of a winning combo
    for combo in combos:
        if len(set(opponent) & set(combo)) == 2:
            # gives a list e.g. [6]
            missing = list(set(combo) - set(opponent))[0] 
            print "index of cell opponent is missing = " + str(missing)
            # if I don't own missing already, block
            if missing not in cpu:
                print "To block..."
                print "CPU as %s plays %s" % (piece, board[missing])
                board[missing] = piece
                return None

    # if turn less than 2 or corners still open...
    if (turn < 2) or (set(corners) & set(board) != 0):
        # pick an untaken corner cell
        missing = list(set(corners) & set(board))[0]
        print "CPU loves corners and so..."
        print "CPU as %s plays %s" % (piece, board[board.index(missing)])
        board[board.index(missing)] = piece
    # naive cpu -- chooses a random unasigned square
    else: 
        while True:
            randomInd = board[randrange(0,9)]
            if (randomInd != "X") and (randomInd != "O"):
                print "In an act of desparation..."
                print "CPU as %s plays %s" % (piece, randomInd)
                board[board.index(randomInd)] = piece
                return

def setup_players():
    """
    sets up which game mode (1 play, 2 play, cpu vs cpu) and pieces
    returns a tuple with (str, str, str)
    """
    # first, figure out who has to play
    while True:
        answers = ("1", "2", "c")
        who = raw_input("players: [1] human, [2] humans, [c]pu only ").lower()
        if who not in answers:
            print "invalid choice. choose the value inside the brackets"
        else:
            break
            # we now have a string "1", "2", "c"

    # then, figure out who is X and O
    pieces = ["X", "O"]
    shuffle(pieces)

    return (who, pieces[0], pieces[1])


if __name__ == "__main__":
    # setup
    id_info = ("", "")
    turn = 1
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    clear_screen()
    print "Tic-Tac-Toe Program\n"
    # split into two steps so that we can easily pass all this info to print
    game_info = setup_players()
    clear_screen()

    # maximum amount of moves in a tictactoe game is 9
    while turn <= 10 and turn >= 1:
        print_view(game_info, board, turn)

        if check_win(board, turn, id_info):
            break

        id_info = cell_chooser(game_info, board, turn)

        turn += 1


    raise SystemExit(0)


# end of file   