from os import system
from random import shuffle, randrange

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

def print_view(turn, board, info):
    # print top status bar
    if info[0] == "2": # two humans
        print "Move #%i -- Player 1 is %s, Player 2 is %s" % (turn, info[1], info[2])
    elif info[0] == "1": # one human, one CPU; computer is always second
        print "Move #%i -- Player 1 is %s, CPU 1 is %s" % (turn, info[1], info[2])
    elif info[0] == "c":
        print "Move #%i -- CPU 1 is %s, CPU 2 is %s" % (turn, info[1], info[2])

    print_board(board)
                
def check_win(turn, ownership):
    """ 
    Given list ownership which is comprised of position strings and ownership strings ('X ' and 'O '), outputs winning piece if there is a winner. 
    Return true(winner) or false
    """
    # winning combinations
    combos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    xs = []
    os = []
    # have to play 5 rounds before a winner can occur
    if turn <= 5:
        return False
  
    # generate list of who owns which square
    for (index, item) in enumerate(ownership):
        if item == "X ":
            xs.append(index)
        elif item == "O ":
            os.append(index)

    players = [xs,os]
    for combo in combos:
        for player in players:
            # from http://stackoverflow.com/questions/1388818/how-can-i-compare-two-lists-in-python-and-return-matches
            if len(set(player) & set(combo)) == 3: 
                if player == xs:
                    print "X Wins!"
                    return True
                elif player == os:
                    print "O Wins!"
                    return True

    # elif winner == "scratch" or turn == 10:
    #     print "no possible winning combination"
    #     printBoard(board)
                
def cell_chooser(player_type, piece, board, turn):
    """
    if human, this is easy; we just change value of cell to the player
    elif robot, give to another func
    returns nothing
    """
    if player_type == "human":
        while True:
            chosen_cell = raw_input("%s's turn: " % piece)
            if (chosen_cell in board): # if valid move...
                # assign current player as the value
                # not always guaranteed to work if not an int
                board[int(chosen_cell) - 1] = piece
                break
            else:
                print "invalid input/move. say a coordinate e.g. 0"
                print_board(board)

    else:
        cpu_player(board, piece, turn)    

def cpu_player(board, piece, turn):
    # winning combinations
    combos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    corners = ["1", "3", "7", "9"]
    shuffle(corners)
    cpu = []
    opponent = []
    
    for (index, item) in enumerate(board):
        if item == piece:
            cpu.append(index)
        elif (item == "O" or item == "X") and (item != piece):
            opponent.append(index)
    
    #print cpu #db
    #print opponent #db
    
    moved = False
    
    for combo in combos:
        if (len(set(cpu) & set(combo)) == 2):
            #print "CONSIDERING WINNING. POSSIBLE MISSING INDEX:" #db
            a = (set(combo) - set(cpu))
            #print a #db
            if len(a & set(opponent)) == 0: # if two in mine similar to combo and the third one isn't in opponent
                #print "cpu two similar" #db
                # get missing -- MUST BE EMPTY      
                missing = list(set(combo) - set(cpu))[0]
                print "CPU as %s plays %s" % (piece, board[missing])
                board[missing] = piece
                moved = True
                break
    # need to be in 2 for loops or else it will stop when it has the chance to win
    # if there is the chance to win and the chance to block, it possibly will take the block
    # this ensures that all the combos are used before going for a block
    if moved == False:
        for combo in combos:
            if len(set(opponent) & set(combo)) == 2: # if two in opponent -- block
                #print "considering opponent 2 simliar" #db
                missing = list(set(combo) - set(opponent))[0] # gives a list e.g. [6]
                print "missing = " + str(missing)
                if missing not in cpu: # if I don't own missing alraedy
                    #print "went for it" #db
                    print "CPU as %s plays %s" % (piece, board[missing])
                    board[missing] = piece
                    moved = True
                    break
    
        if (turn < 2) or (set(corners) & set(board) != 0): # if they are still open
            #print "corner move" #db
            # get the string of the remaining square in board
            # pairs in corners that are in board
            #print "TAKING [0] OF THIS LIST" #db
            #print list(set(corners) & set(board)) #db
            missing = list(set(corners) & set(board))[0]
            print "CPU as %s plays %s" % (piece, board[board.index(missing)])
            board[board.index(missing)] = piece
        else:
            #print "naive method" # debug
            # naive cpu -- chooses a random unasigned square
            while True:
                randomInd = board[randrange(0,9)]
                if (randomInd != "X") and (randomInd != "O"):
                    print "CPU as %s plays %s" % (piece, randomInd)
                    board[board.index(randomInd)] = piece
                    break

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
    turn = 1
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

    system("cls")
    print "Tic-Tac-Toe Program\n"
    # split into two steps so that we can easily pass all this info to print
    game_info = setup_players()
    system('cls')
    gametype, player1, player2 = game_info
    # maximum amount of moves in a tictactoe game is 9
    while turn <= 10 and turn >= 1: 
        if check_win(turn, board):
            break
            
        print_view(turn, board, game_info)

        if gametype == "2":
             # if turn is even...
            if (turn % 2 == 1):
                cell_chooser("human", player1, board, turn)
                system('cls') # clear screen -- windows only!
            # else if turn is odd...
            else: 
                cell_chooser("human", player2, board, turn)
                system('cls') # clear screen -- windows only!
        elif gametype == "1":
            if (turn % 2 == 1):
                cell_chooser("human", player1, board, turn)
                system('cls') # clear screen -- windows only!
            else:
                cell_chooser("cpu", player2, board, turn)
        elif gametype == "c":
            if (turn % 2 == 1):
                cell_chooser("cpu", player1, board, turn)
            else:
                cell_chooser("cpu", player2, board, turn)

        turn += 1



    raise SystemExit(0)


# end of file   