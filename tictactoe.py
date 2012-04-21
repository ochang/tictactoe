# add AI
# add win counter and a easy way to start another game
# build interface to choose 2 humans or 1 human or 2 cpu
# migrate stuff to classes. also: figure out if I should to that

from random import shuffle,randrange

def printBoard(board):
	""" Prints an ASCII art representation of a tictactoe grid. Assumed that 'board' is given in a list fomat that goes down the first row's colums and then proceeds to second row i.e. [first row cells, second row cells, third row cells]. """
	index = 0
	print "----------------------------------------"
	for x in range(3): # for every row...
		for x in range(3): # for every column (left, center, right)...
			if index == 0 or index == 3 or index == 6:
				left = board[index]
			elif index == 1 or index == 4 or index == 7:
				center = board[index]
			elif index == 2 or index == 5 or index == 8:
				right = board[index]
			else:
				print "unexpected index"
			index += 1 # incerement so next pass is for the next cell
		print "|     %s     |     %s     |     %s     |" % (left,center,right)
		print "----------------------------------------"
				
def checkWin(ownership):
	""" Given list ownership which is comprised of position strings and ownership strings ('X ' and 'O '), outputs winning piece if there is a winner. """
	
	# improvements:
		# check what happens in a scratch game
	
	combos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] # winning combinations
	
	# sort ownership into two lists
	xs = []
	os = []
	
	for (index, item) in enumerate(ownership):
		if item == "X ":
			xs.append(index)
		elif item == "O ":
			os.append(index)
		else:
			pass
	#print xs # debug
	#print os # debug
	
	
	# if (len(xs) < 3) or (len(os) < 3):
		# return 0
	# else:	
	players = [xs,os]
	for combo in combos:
		for player in players:
			if len(set(player) & set(combo)) == 3: # from here http://stackoverflow.com/questions/1388818/how-can-i-compare-two-lists-in-python-and-return-matches
				if player == xs:
					return "X"
				elif player == os:
					return "O"
				
def chooser(playerType,piece,board):
	printBoard(board)
	# sets up the correct prompt
	if piece == "X ":
		prompt = "X's turn: "
	elif piece == "O ":
		prompt = "O's turn: "

	# sets the correct player
	if playerType == "human":
		doMove = raw_input(prompt).upper()
		if doMove in board: # if valid move...
			board[board.index(doMove)] = piece # assign current player as the value of coordIndex
		else:
			print "invalid input/move. go again, %s" % piece
			printBoard(board)
	elif playerType == "cpu":
		cpu_player(board,piece)	

def game_type():
	while True:
		answers = ("1","2","c")
		whosPlaying = raw_input("players: [1] human, [2] humans, [c]pu only ")
		if whosPlaying not in answers:
			print "invalid choice. choose the value inside the brackets"
		else:
			break
	return whosPlaying

def cpu_player(board,piece): # turn, player eventually
	# start by choosing a random unassigned square and return its index
	
	#choose random square
	
	while True:
		x = board[randrange(0,9)]
		if (x != "X ") and (x != "O "):
			print "CPU playing %s" % x
			board[board.index(x)] = piece # assign current player as the value of coordIndex
			break
		else:
			pass

def print_players(gametype,shuffled):
	print "\n"
	if gametype == "2": # two humans
		print "Player 1 is %s" % shuffled[0]
		print "Player 2 is %s" % shuffled[1]
	elif gametype == "1": # one human, one CPU; computer is always second
		print "Player 1 is %s" % shuffled[0]
		print "CPU 1 is %s" % shuffled[1]
	elif gametype == "c":
		print "CPU 1 is %s" % shuffled[0]
		print "CPU 2 is %s" % shuffled[1]	


		
turn = 1
board = ["LT","CT","RT","LC","CC","RC","LB","CB","RB"]
shuffled = ["X ", "O "]
shuffle(shuffled)

print "Tic-Tac-Toe Program"	
gametype = game_type() # returns String 1,2,c

print_players(gametype,shuffled)
	
while turn <= 10 and turn > 0: # maximum amount of moves in a tictactoe game is 9
	if turn > 5: # have to play 5 rounds before a winner can occur
		winner = checkWin(board)
		if winner == "X":
			print "X Wins!"
			break
		elif winner == "O":
			print "O Wins!"
			break
		elif winner == "scratch" or turn == 10:
			print "no possible winning combination"
			break
		else:
			pass
		
	print "\n\nMove #%i" % turn	
	if gametype == "2":
		if (turn % 2 == 1): # if turn is even...
			chooser("human",shuffled[0],board)
		else: # if turn is odd...
			chooser("human",shuffled[1],board)
	elif gametype == "1":
		if (turn % 2 == 1): # if turn is even...
			chooser("human",shuffled[0],board)
		else: # if turn is odd...
			chooser("cpu",shuffled[1],board)
	elif gametype == "c":
		if (turn % 2 == 1): # if turn is even...
			chooser("cpu",shuffled[0],board)
		else: # if turn is odd...
			chooser("cpu",shuffled[1],board)	
	turn += 1
		



# end of file	