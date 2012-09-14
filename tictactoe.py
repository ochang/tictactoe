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
            if i in (0, 3, 6):
                left = board[i]
            elif i in (1, 4, 7):
                center = board[i]
            elif i in (2, 5, 8):
                right = board[i]
            else:
                print "unexpected index"
            i += 1 # incerement so next pass is for the next cell
        print "|     %s     |     %s     |     %s     |" % (left,center,right)
        print "-------------------------------------"

def print_view(turn, board):
    # if who == "2": # two humans
    #     print "Player 1 is %s" % pieces[0]
    #     print "Player 2 is %s" % pieces[1]
    # elif who == "1": # one human, one CPU; computer is always second
    #     print "Player 1 is %s" % pieces[0]
    #     print "CPU 1 is %s" % pieces[1]
    # elif who == "c":
    #     print "CPU 1 is %s" % pieces[0]
    #     print "CPU 2 is %s" % pieces[1]

    # system('cls') # clear screen -- windows only!
    print "Move #%i -- " % turn
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
        chosen_cell = raw_input("%s's turn: " % piece)
        if chosen_cell in board: # if valid move...
            # assign current player as the value
            # not always guaranteed to work if not an int
            board[int(chosen_cell)] = piece 
        else:
            print "invalid input/move. say a coordinate e.g. 0"
            print_board(board)

    else:
        cpu_player(board, piece, turn)    

def cpu_player(board,CPUpiece,turn):
    combos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] # winning combinations
    cpu = []
    opponent = []
    
    for (index, item) in enumerate(board):
        if item == CPUpiece:
            cpu.append(index)
        elif (item == "O " or item == "X ") and (item != CPUpiece):
            opponent.append(index)
    
    #print cpu #db
    #print opponent #db
    
    corners = ["LT", "RT", "LB", "RB"]
    shuffle(corners)
    # middle = 4
    # sides = [1, 3, 5, 7]
    # shuffle(sides)
    
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
                print "CPU as %splays %s" % (CPUpiece, board[missing])
                board[missing] = CPUpiece
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
                    print "CPU as %splays %s" % (CPUpiece, board[missing])
                    board[missing] = CPUpiece
                    moved = True
                    break
    
    if moved == False:
        if (turn < 2) or (set(corners) & set(board) != 0): # if they are still open
            #print "corner move" #db
            # get the string of the remaining square in board
            # pairs in corners that are in board
            #print "TAKING [0] OF THIS LIST" #db
            #print list(set(corners) & set(board)) #db
            missing = list(set(corners) & set(board))[0]
            print "CPU as %splays %s" % (CPUpiece, board[board.index(missing)])
            board[board.index(missing)] = CPUpiece
        else:
            #print "naive method" # debug
            # naive cpu -- chooses a random unasigned square
            while True:
                randomInd = board[randrange(0,9)]
                if (randomInd != "X ") and (randomInd != "O "):
                    print "CPU as %splays %s" % (CPUpiece, randomInd)
                    board[board.index(randomInd)] = CPUpiece
                    break
    else:
        pass

def setup_players():
    """
    sets up which game mode (1 play, 2 play, cpu vs cpu) and pieces
    returns a tuple with (str, str, str)
    """
    # first, figure out who has to play
    while True:
        answers = ("1","2","c")
        who = raw_input("players: [1] human, [2] humans, [c]pu only ").lower()
        if who not in answers:
            print "invalid choice. choose the value inside the brackets"
        else:
            break
            # we now have a string "1", "2", "c"

    # then, figure out who is X and O
    pieces = ["X ", "O "]
    shuffle(pieces)

    return (who, pieces[0], pieces[1])


if __name__ == "__main__":
    # setup
    turn = 1
    # board = ["LT","CT","RT","LC","CC","RC","LB","CB","RB"]
    board = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]

    system("cls")
    print "Tic-Tac-Toe Program\n"
    gametype, player1, player2 = setup_players()
    
    # maximum amount of moves in a tictactoe game is 9
    while turn <= 10 and turn >= 1: 
        if check_win(turn, board):
            break
            
        print_view(turn, board)
        # break


        if gametype == "2":
            if (turn % 2 == 1): # if turn is even...
                cell_chooser("human", player1, board, turn)
            else: # if turn is odd...
                cell_chooser("human", player2, board, turn)
        elif gametype == "1":
            if (turn % 2 == 1): # if turn is even...
                cell_chooser("human", player1, board, turn)
            else: # if turn is odd...
                cell_chooser("cpu", player2, board, turn)
        elif gametype == "c":
            if (turn % 2 == 1): # if turn is even...
                cell_chooser("cpu", player1, board, turn)
            else: # if turn is odd...
                cell_chooser("cpu", player2, board, turn)
        turn += 1



    raise SystemExit(0)


# end of file   