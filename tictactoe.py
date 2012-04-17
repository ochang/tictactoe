
from random import randrange
def printBoard(possStrings):
	# !!!! make sure possStrings is formatted to correctly use this function
	# has to be in form which is top row (LT, CT, RT) -> center -> bottom row
	# print the coordinates of blanks
	print "----------------------------------------" # first line
	
	# start working on topRow
	index = 1
	for x in range(3): # do these instructions 3 times; once for each row
		left = " " # reset these values to blank and add a space to make blank and filled lines have the same length
		center = " " 
		right = " "
		for z in range(3): # for every column in the working row, do this
			currEval = possStrings[index] # starts at possStrings[1] = a string that describes the owner: "", "X", or "O"
			if currEval == "": # if there is no owner
				index += 2 # then move to the next position's ownership
			elif currEval != "": # if there is an owner
				if index == (1 or 7 or 13): # if the left block
					left = currEval
				elif index == (3 or 9 or 15): # if center block
					center = currEval
				elif index == (5 or 11 or 17): # if right block
					right = currEval
				index += 2
			print "|     %s     |     %s     |     %s     |" % (left,center,right)		
	print "----------------------------------------" # last line	

print "Tic-Tac-Toe Program"
print "To play, take turns playing the coordinates below"


print "|     LT     |     CT     |     RT     |" # 5 spaces
print "|     LC     |     CC     |     RC     |"
print "|     LB     |     CB     |     RB     |"

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
		possStrings[(possStrings.index(doMove) + 1)] = currPlayer # get the index of the last move, puts the player as the owner of that tile in the next item in possStrings
		possMoves.remove(doMove)
		printBoard(possStrings)
		turn += 1
		#print possMoves
		#print possStrings
	else:
		print "invalid input/move"


		
		
def checkWin():
	pass

















		