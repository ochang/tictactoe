
from random import randrange
def printBoard(ownerList):
	print "----------------------------------------" # first line
	
	
	
	# start working on topRow
	index = 0
	
	
	
	while index < 9:
		left = " " # reset these values to blank and add a space to make blank and filled lines have the same length
		center = " " 
		right = " "
		
		for x in range(3):
			print str(index) + " INDEXXX"
			currEval = ownerList[index] # returns a string that describes the owner: "", "X", or "O"
			if currEval == "": # if there is no owner
				index += 1 # then move to the next position's ownership
			elif currEval != "": # if there is an owner
				if index == (0 or 3 or 6): # if the left block
					left = currEval
				elif index == (1 or 4 or 7): # if center block
					center = currEval
				elif index == (2 or 5 or 8): # if right block
					right = currEval
				index += 1
			
		print "|     %s     |     %s     |     %s     |" % (left,center,right)
		print "----------------------------------------"

		
		
		
		
		
		
		
		
		
		
		
		
		
print "Tic-Tac-Toe Program"
print "To play, take turns playing the coordinates below"

possMoves = ["LT","CT","RT","LC","CC","RC","LB","CB","RB"]
ownership = ["","","","","","","","",""]

# initial board print -- testing component of printBoard()
i = 0
print "----------------------------------------"
while i < 9:
		left = "left" # reset these values to blank and add a space to make blank and filled lines have the same length
		center = "center" 
		right = "right"
		
		i+=3
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

















		