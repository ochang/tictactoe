
from random import randrange
def printBoard(board):
	index = 0
	print "----------------------------------------"
	for x in range(3):
		for x in range(3):
			if index == 0 or index == 3 or index == 6:
				left = board[index]
			elif index == 1 or index == 4 or index == 7:
				center = board[index]
			elif index == 2 or index == 5 or index == 8:
				right = board[index]
			else:
				print "unexpected index"
			index += 1
		print "|     %s     |     %s     |     %s     |" % (left,center,right)
		print "----------------------------------------"
				
def checkWin(ownership):
	xs = 
	os = 

	# split into two lists which are ordered
	# all non-owned squares = 25
	# list1 = all indices that x owns e.g. [0,1]
	# list 2 = all indices that o owns e.g. [2,4]
	# if len(list) < 3: skip; can't possibly be a winner
	# if somebody owns one of eight three-digit combinations then winner
	# combos = 012,345,687,036,147,258,048,246
	
	# obvious idea stolen from here http://en.literateprograms.org/Tic_Tac_Toe_(Python)#chunk use:tictactoe.py
	# store the combos as lists -- duh
	combos = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
	for combo in combos:
		if # elements of combo are present in ownership: win condition
		
print "Tic-Tac-Toe Program"
print "To play, take turns playing the coordinates below"

possMoves = ["LT","CT","RT","LC","CC","RC","LB","CB","RB"]
ownership = ["LT","CT","RT","LC","CC","RC","LB","CB","RB"]

printBoard(possMoves)

# example board
#print "|     LT 0     |     CT 1     |     RT 2     |" 
#print "|     LC 3     |     CC 4     |     RC 5     |"
#print "|     LB 6     |     CB 7     |     RB 8     |"



# decides initial turn
# imported from random module -- gives 1 or 2 pseudorandomly
turn = randrange(1,3) # 1 = x first, 2 = o first


#def input(possMoves): # takes a list of possible moves
while turn < 10:
	# chooses which prompt to show; only changes on successful move
	if (turn % 2) == 1:  # if turn is even
		prompt = "\nX's turn: "
		currPlayer = "X " # space is to ensure consistent formatting with the two letter coordinates
	else: # effectively, when turn is odd
		prompt = "\nO's turn: "
		currPlayer = "O "
		
	doMove = (raw_input(prompt)).upper() # gets a string as an input and converts to upeprcase to match possMoves
	if doMove in possMoves:
		coordIndex = possMoves.index(doMove)
		ownership[coordIndex] = currPlayer # get the index of the last move, puts the player as the owner of that space
		possMoves[coordIndex] = ""
		printBoard(ownership)
		turn += 1
		#print possMoves
		#print possStrings
	else:
		print "invalid input/move"



# end of file	