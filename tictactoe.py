# add win counter and a easy way to start another game
# migrate stuff to classes. also: figure out if I should to that
# still possible to win if AI picks wrong corners at start versus a human
# all cpu vs. cpu games play out exactly the same
# add prompt to play again after game? (who wants to play that much tictactoe?)

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
	
	combos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] # winning combinations
	
	xs = []
	os = []
	
	for (index, item) in enumerate(ownership):
		if item == "X ":
			xs.append(index)
		elif item == "O ":
			os.append(index)
	#print xs # debug
	#print os # debug

	players = [xs,os]
	for combo in combos:
		for player in players:
			if len(set(player) & set(combo)) == 3: # from here http://stackoverflow.com/questions/1388818/how-can-i-compare-two-lists-in-python-and-return-matches
				if player == xs:
					return "X"
				elif player == os:
					return "O"
				
def chooser(playerType,piece,board,turn):
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
		cpu_player(board,piece,turn)	

def game_type():
	while True:
		answers = ("1","2","c")
		whosPlaying = raw_input("players: [1] human, [2] humans, [c]pu only ")
		if whosPlaying not in answers:
			print "invalid choice. choose the value inside the brackets"
		else:
			break
	return whosPlaying

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
				#print "opponent 2 simliar" #db
				missing = list(set(combo) - set(opponent))[0]
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
			print "vvvvv WINNING BOARD vvvvv"
			printBoard(board)
			break
		elif winner == "O":
			print "O Wins!"
			print "vvvvv WINNING BOARD vvvvv"
			printBoard(board)
			break
		elif winner == "scratch" or turn == 10:
			print "no possible winning combination"
			printBoard(board)
			break
		else:
			pass
		
	print "\n\nMove #%i" % turn	
	if gametype == "2":
		if (turn % 2 == 1): # if turn is even...
			chooser("human",shuffled[0],board,turn)
		else: # if turn is odd...
			chooser("human",shuffled[1],board,turn)
	elif gametype == "1":
		if (turn % 2 == 1): # if turn is even...
			chooser("human",shuffled[0],board,turn)
		else: # if turn is odd...
			chooser("cpu",shuffled[1],board,turn)
			#print "CPU is " + shuffled[1] #db
	elif gametype == "c":
		if (turn % 2 == 1): # if turn is even...
			chooser("cpu",shuffled[0],board,turn)
			#print "CPU is " + shuffled[0] #db
		else: # if turn is odd...
			chooser("cpu",shuffled[1],board,turn)
			#print "CPU is " + shuffled[1] #db
	turn += 1
		



# end of file	