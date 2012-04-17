


print "Tic-Tac-Toe Program"
print "To play, take turns playing the coordinates below"

print "--------------------------"
print "|	LT	|	CT	|	RT	|"
print "|	LC	|	CC	|	RC	|"
print "|	LB	|	CB	|	RB	|"
print "--------------------------"

possMoves = [LT,CT,RT,LC,CC,RC,LB,CB,RB]
top = ["","",""]
middle = ["","",""]
bottom = ["","",""]

# add random element to who goes first
turn = 1 # 1 = x first, 2 = o first

#def input(possMoves): # takes a list of possible moves
while True:
	if (turn % 2) == 1  # if turn is even
		print "x's turn"
	else:
		print "y's turn"
		
	doMove = raw_input("move: ")
	if doMove in possMoves
		parser1(doMove)	
		return doMove
		possMoves.remove(possMoves.index(doMove))
		turn += 1
	else:
		print "invalid input"
		return 0

def parser1(x,topList,centerList,bottomList)):
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
			
		elif otherHalf == 1 # CT
		elif otherHalf == 2 # RT
	elif toParse == "C":
	elif toParse == "B":
		




















		