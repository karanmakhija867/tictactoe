from Terminal_test import Terminal_test
from sys import maxsize


def test_print(state):
	for i in range(4):
		for j in range(4):
			print state.board[i][j],
		print  

def minimax(depth,state,maximisingagent):
	
	ttest = Terminal_test(state)
	if ttest[0]:
		if ttest[1] > 0:
			return float(ttest[1] -float(depth)/20)
		elif ttest[1] < 0:
			return float(ttest[1] +float(depth)/20)
		else :
			return ttest[1]	
			

	if maximisingagent:

		bestValue = -maxsize
		for i in range(4):
			if state.col[i] < 4:
				state.board[state.col[i]][i] = 'B' 
				state.col[i] += 1
				val = minimax(depth+1,state,False)
				bestValue = max(bestValue,val)
				state.col[i] -= 1
				state.board[state.col[i]][i] = '_' 
		return bestValue 	
	else:
		bestValue = maxsize
		for i in range(4):
			if state.col[i] < 4:
				state.board[state.col[i]][i] = 'G' 
				state.col[i] += 1
				val = minimax(depth+1,state,True)
				bestValue = min(bestValue,val)
				state.col[i] -= 1
				state.board[state.col[i]][i] = '_' 
				
		return bestValue












