# add AI
# change possMoves and ownership -- just use one
# add win counter and a easy way to start another game

from random import randrange

class compPlayer: # a = compPlayer() -> a(ownership)
	def __init__(self,ownership):
		pass
	# the main objectives of the player are (in order of importance):
		# 1. stop the other player from winning
		# 2. win
	def strategyChoose(self):
		pass
	def blockStrategy(self):
		pass
	def winStrategy(self):
		pass



def printBoard(board):
	"""Prints a ASCII art representation of a tictactoe grid. Assumed that 'board' is given in a list fomat that goes down the first row's colums and then proceeds to second row i.e. [first row cells, second row cells, third row cells]. """
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
	""" Given list ownership which is comprised of position strings and ownership strings ('X ' and 'O ', returns 0 = no winner, 1 = x-winner, 2 = o-winner. """
	
	# improvements:
		# check what happens in a scratch game
			# stop the game if there can no longer be a winner
		# if len(list) < 3: skip; can't possibly be a winner
	
	combos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]] # winning combinations; constant
	
	# sort ownership into two lists
	xs = [] # the indices of the positions in 'ownership' that x owns
	os = [] # same but for o
	index = 0
	while index < 9:
		if ownership[index] == "X ":
			xs.append(index)
		elif ownership[index] == "O ":
			os.append(index)
		else:
			pass
		index += 1
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
					return 1
				elif player == os:
					return 2
				else:
					print "unexpected winner"
				
			
		
print "Tic-Tac-Toe Program"
print "To play, take turns playing the coordinates below"

ownership = ["LT","CT","RT","LC","CC","RC","LB","CB","RB"]

printBoard(ownership)

# example board
#print "|     LT 0     |     CT 1     |     RT 2     |" 
#print "|     LC 3     |     CC 4     |     RC 5     |"
#print "|     LB 6     |     CB 7     |     RB 8     |"



# decides initial turn
# imported from random module -- gives 1 or 2 pseudorandomly
turn = randrange(1,3) # 1 = x first, 2 = o first


while turn < 10:
	# chooses which prompt to show; only changes on successful move
	if (turn % 2) == 1:  # if turn is even...
		prompt = "\nX's turn: "
		currPlayer = "X " # space is to ensure consistent formatting with the two letter coordinates
	else: # if turn is odd...
		prompt = "\nO's turn: "
		currPlayer = "O "
		
	doMove = (raw_input(prompt)).upper() # gets a string as an input and converts to upeprcase to match possMoves; example: LT, LC, LB, RB...
	if (doMove in ownership) and (doMove != ""): # if valid move...
		coordIndex = ownership.index(doMove) # coordIndex = index of that move in ownership
		ownership[coordIndex] = currPlayer # assign current player as the value of coordIndex in ownership
		printBoard(ownership) # print board with changes in ownership
		winner = checkWin(ownership) # run checkWin()
		#print winner # debug
		if winner == 1:
			print "X wins!"
			break
		elif winner == 2:
			print "O wins!"
			break
		turn += 1
		#print possMoves
		#print possStrings
	else:
		print "invalid input/move. go again, %s" % currPlayer
		printBoard(ownership)



# end of file	