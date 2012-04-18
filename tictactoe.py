
from random import randrange
def printBoard(ownerList):

		
		
		
		
		
		
		
		
		
		
		
		
		
print "Tic-Tac-Toe Program"
print "To play, take turns playing the coordinates below"

possMoves = ["LT","CT","RT","LC","CC","RC","LB","CB","RB"]
ownership = ["","","","","","","","",""]

# initial board print -- testing component of printBoard()
index = 0
print "----------------------------------------"
for x in range(3):
	for x in range(3):
		if index == 0 or index == 3 or index == 6:
			left = possMoves[index]
		elif index == 1 or index == 4 or index == 7:
			center = possMoves[index]
		elif index == 2 or index == 5 or index == 8:
			right = possMoves[index]
		else:
			print "wrong"
		index += 1
	print "|     %s     |     %s     |     %s     |" % (left,center,right)
	print "----------------------------------------"


#print "|     LT     |     CT     |     RT     |" # 5 spaces
#print "|     LC     |     CC     |     RC     |"
#print "|     LB     |     CB     |     RB     |"



# initial turn
# imported from random module -- gives 1 or 2 pseudorandomly
turn = randrange(1,3) # 1 = x first, 2 = o first


#def input(possMoves): # takes a list of possible moves
while turn < 10:
	# chooses which prompt to show; only changes on successful move
	if (turn % 2) == 1:  # if turn is even
		prompt = "X's turn: "
		currPlayer = "X"
	else: # effectively, when turn is odd
		prompt = "O's turn: "
		currPlayer = "O"
		
	doMove = (raw_input(prompt)).upper() # gets a string as an input and converts to upeprcase to match possMoves
	if doMove in possMoves:
		coordIndex = possMoves.index(doMove)
		ownership[coordIndex] = currPlayer # get the index of the last move, puts the player as the owner of that space
		print ownership
		possMoves[coordIndex] = ""
		print possMoves
		printBoard(ownership)
		turn += 1
		#print possMoves
		#print possStrings
	else:
		print "invalid input/move"


		
		
def checkWin():
	pass

















		