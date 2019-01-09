from Terminal_test import Terminal_test

def alphabeta(a,b,depth,state,maximisingagent):
	

	ttest = Terminal_test(state)
	if ttest[0]:
		if ttest[1] > 0:
			return float(ttest[1] -float(depth)/20)
		elif ttest[1] < 0:
			return float(ttest[1] +float(depth)/20)
		else :
			return ttest[1]
	
	if maximisingagent:
		for i in range(4):
			if state.col[i] < 4:
				state.board[state.col[i]][i] = 'B'
				state.col[i] += 1
				a = max(a,alphabeta(a,b,depth+1,state,False))
				state.col[i] -= 1
				state.board[state.col[i]][i] = '_'
				if a >= b:
					break
				
		return a

	else:
		for i in range(4):
			if state.col[i] < 4:
				state.board[state.col[i]][i] = 'G'
				state.col[i] += 1
				b = min(b,alphabeta(a,b,depth+1,state,True))
				state.col[i] -= 1
				state.board[state.col[i]][i] = '_'
				if a >= b:
					break
				
			
		return b


