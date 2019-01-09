import turtle as t
from minimax import minimax
from alphabeta import alphabeta
from sys import maxsize
from Terminal_test import Terminal_test


class node:
	def __init__(self):
			self.board = [ ['_' for j in range(4)] for i in range(4)]
			self.col = [0,0,0,0]

board = [ ['_' for i in range(4)] for j in range(4)]
x_coord = -200
y_coord = 150
length = 100
rows = 4
cols = 4
col = [0,0,0,0]

start = node()
turn = True



def test_print(state):
	for i in range(4):
		for j in range(4):
			print state.board[i][j],
		print 
	print "\n"

def create_board():
	for i in range(rows):
		t.penup()
		t.setposition(x_coord,y_coord-length*i)
		t.pendown()
		for i in range(cols):
			create_square()
			t.forward(length)

def create_square():
	for i in range(4):
		t.fd(length)
		t.right(90)

def create_game():
	for row in range(len(board)):
		for col in range(len(board[row])):
			if board[row][col] == 'B':
				t.penup()
				t.setposition(x_coord+length*col+length//2,y_coord-length*row)
				t.pendown()
				t.color("blue")
				t.begin_fill()
				t.circle(-length//2)
				t.end_fill()
			elif board[row][col] == 'G':
				t.penup()
				t.setposition(x_coord+length*col+length//2,y_coord-length*row)
				t.pendown()
				t.color("green")
				t.begin_fill()
				t.circle(-length//2)
				t.end_fill()

			

def get_click(click_x,click_y):
	
		
		global turn
		j = (click_x-x_coord)//length
		i = (y_coord-click_y)//length

		if int(j) in range(cols):
			if int(i) == col[int(j)]:
				board[int(i)][int(j)] = 'G'
				col[int(j)] +=1
				create_game()
				turn =True
	




t.setup(600,600)
t.screensize(600,600)
t.setworldcoordinates(-300,-300,300,300)
t.speed(0)
t.hideturtle()
create_board()

while(True):
	
	if turn:
		t.onscreenclick(None)
		t.update()
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
		board = start.board
		col = start.col
		create_game()
		turn = False 		 		
	else:
		t.onscreenclick(get_click)
		t.update()
		start.board = board
		start.col = col
	


	if Terminal_test(start)[0] == True:
		break
		
		
if Terminal_test(start)[1] >0:
	print "Computer Wins"
elif Terminal_test(start)[1] <0:
	print "Human Wins"
else:
	print "Draw"


t.delay(3000)	




