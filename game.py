from minimax import minimax
from alphabeta import alphabeta
from sys import maxsize
from Terminal_test import Terminal_test


class node:
	def __init__(self):
			self.board = [ ['_' for j in range(4)] for i in range(4)]
			self.col = [0,0,0,0]



		
def test_print(state):
	for i in range(4):
		for j in range(4):
			print state.board[i][j],
		print 
	print "\n"	
			

start = node()
turn = False
while(not Terminal_test(start)[0]):
	if turn:
		max_val = -maxsize
		index = -4
		for i in range(4):
			if start.col[i] < 4:
				start.board[start.col[i]][i] = 'B' 
				start.col[i] += 1
				testvalue = alphabeta(-maxsize,maxsize,0.0,start,False)
				#print testvalue
				max_val = max(max_val,testvalue) 
				if  max_val == testvalue:
					index = i
				#print index	
				start.col[i] -= 1
				start.board[start.col[i]][i] = '_' 
			

		start.board[start.col[index]][index] = 'B'
		start.col[index] +=1
		turn = False 
		test_print(start)		 		
	
	else:
		hum_input = input("Enter column")
		start.board[start.col[hum_input]][hum_input] = 'G'
		start.col[hum_input] += 1
		turn = True
		test_print(start)
		
if Terminal_test(start)[1] >0:
	print "Computer Wins"
elif Terminal_test(start)[1] <0:
	print "Human Wins"
else:
	print "Draw"








		





