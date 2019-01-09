score = {'B':1.0,'G':-1.0,'D':0.0}

# class node:
# 	def __init__(self):
# 			self.board = [ ['_' for j in range(4)] for i in range(4)]
# 			self.col = [0,0,0,0]

def Terminal_test(state):
	
	for i in range(4):
		if state.board[i][0] == state.board[i][1] and state.board[i][1] == state.board[i][2] and state.board[i][0]!='_': 
			#print "horizontal line found"
			return True, score[state.board[i][0]]
		if state.board[i][1] == state.board[i][2] and state.board[i][2] == state.board[i][3] and state.board[i][1]!='_':
			return True, score[state.board[i][1]]
	
	for j in range(4):
		if state.board[0][j] == state.board[1][j] and state.board[1][j] == state.board[2][j] and state.board[0][j]!='_':
			return True, score[state.board[0][j]]
		
		if state.board[1][j] == state.board[2][j] and state.board[2][j] == state.board[3][j] and state.board[1][j]!='_':
			return True, score[state.board[1][j]]
	
	for i in range(2):
		for j in range(2):
			if state.board[i][j]==state.board[i+1][j+1] and state.board[i+1][j+1]==state.board[i+2][j+2] and state.board[i][j]!='_':
				return True, score[state.board[i][j]]

	for i in range(2,4):
		for j in range(2):
			if state.board[i][j]==state.board[i-1][j+1] and state.board[i-1][j+1]==state.board[i-2][j+2] and state.board[i][j]!='_':
				return True, score[state.board[i][j]]

	for i  in range(4):
		for j in range(4):
			if state.board[i][j] == '_':
				return False,999

	return True,score['D']


# state = node()
# state.board =[['B','B','G','G'],['G','B','B','B'],['B','B','G','_'],['_','_','_','_']]			
# state.col = [3,3,3,2]
# print type(Terminal_test(state))	