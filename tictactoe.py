
from random import randrange

print "Tic-Tac-Toe Program"
print "To play, take turns playing the coordinates below"


print "|	LT	|	CT	|	RT	|"
print "|	LC	|	CC	|	RC	|"
print "|	LB	|	CB	|	RB	|"

possMoves = [["LT",""],["CT",""],["RT",""],["LC",""],["CC",""],["RC",""],["LB",""],["CB",""],"RB",""]]

# initial turn
# imported from random module -- gives 1 or 2 pseudorandomly
turn = randrange(1,3) # 1 = x first, 2 = o first


#def input(possMoves): # takes a list of possible moves
while turn <= 9:
	if (turn % 2) == 1:  # if turn is even
		prompt = "x's turn: "
	else:
		prompt = "y's turn: "
		
	doMove = raw_input(prompt)
	if doMove in possMoves:
		#parser1(doMove)	
		print doMove
		possMoves.remove(doMove)
		turn += 1
	else:
		print "invalid input/move"

def parser1(x,topList,centerList,bottomList):
	x = list(x) # from http://mail.python.org/pipermail/tutor/2005-August/040892.html
	if x[0] == "L":
		parser2(x[1],0,topList)
	elif x[0] == "C":
		parser2(x[1],1,centerList)
	elif x[0] == "R":
		parser2(x[1],2,bottomList)
	else:
		print "error in parsing"
	
def parser2(toParse,otherHalf,moveList):
	if toParse == "T":
		if otherHalf == 0: # LT
			pass
		elif otherHalf == 1: # CT
			pass
		elif otherHalf == 2: # RT
			pass
	elif toParse == "C":
		pass
	elif toParse == "B":
		pass




















		