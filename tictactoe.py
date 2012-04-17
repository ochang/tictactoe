
from random import randrange

print "Tic-Tac-Toe Program"
print "To play, take turns playing the coordinates below"


print "|	LT	|	CT	|	RT	|"
print "|	LC	|	CC	|	RC	|"
print "|	LB	|	CB	|	RB	|"

possMoves = ["LT","CT","RT","LC","CC","RC","LB","CB","RB"]
possStrings = ["LT","","CT","","RT","","LC","","CC","","RC","","LB","","CB","","RB",""]

# initial turn
# imported from random module -- gives 1 or 2 pseudorandomly
turn = randrange(1,3) # 1 = x first, 2 = o first


#def input(possMoves): # takes a list of possible moves
while turn <= 9:
	# chooses which prompt to show; only changes on successful move
	if (turn % 2) == 1:  # if turn is even
		prompt = "X's turn: "
		currPlayer = "X"
	else: # effectively, when turn is odd
		prompt = "O's turn: "
		currPlayer = "O"
		
	doMove = (raw_input(prompt)).upper() # gets a string as an input and converts to upeprcase to match possMoves
	if doMove in possMoves:
		possStrings[(possStrings.index(doMove) + 1)] = currPlayer
		possMoves.remove(doMove)
		turn += 1
		#print possMoves
		#print possStrings
	else:
		print "invalid input/move"

def printBoard()
	pass
		
def checkWin():
	pass

















		