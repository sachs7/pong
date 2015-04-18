tes = [[1, 3, 2, 5, 7, 9, 4, 6, 8],
	[4, 9, 8, 2, 6, 1, 3, 7, 5],
	[7, 5, 6, 3, 8, 4, 2, 1, 9],
	[6, 4, 3, 1, 5, 8, 7, 9, 2],
	[5, 2, 1, 7, 9, 3, 8, 4, 6],
	[9, 8, 7, 4, 2, 6, 5, 3, 1],
	[2, 1, 4, 9, 3, 5, 6, 8, 7],
	[3, 6, 5, 8, 1, 7, 9, 2, 4],
	[8, 7, 9, 6, 4, 2, 1, 3, 5]]
	
"""tes = [[5, 3, 4, 6, 7, 8, 9, 1, 2], 
		[6, 7, 2, 1, 9, 5, 3, 4, 8],
		[1, 9, 8, 3, 4, 2, 5, 6, 7],
		[8, 5, 9, 7, 6, 1, 4, 2, 3],
		[4, 2, 6, 8, 5, 3, 7, 9, 1],
		[7, 1, 3, 9, 2, 4, 8, 5, 6],
		[9, 6, 1, 5, 3, 7, 2, 8, 4],
		[2, 8, 7, 4, 1, 9, 6, 3, 5],
		[3, 4, 5, 2, 8, 6, 1, 7, 9]]
"""			   
def validSolution(board):
	
	if board == []:
		return False	
		
	# To count repeating pattern of numbers in ROWS 
	def first_tbyt(board):
		tbyt = [ board[j][i] for j in range(3) for i in range(3) ] #first 3x3 matrix
		return result(tbyt)
		
	def center_tbyt(board):
		tbyt = [ board[j][i] for j in range(3,6) for i in range(3,6) ] # center 3x3 matrix
		return result(tbyt)
		
	def bright_tbyt(board):
		tbyt = [ board[j][i] for j in range(6,9) for i in range(6,9) ] # bottom right 3x3 matrix
		return result(tbyt)
		
	def bleft_tbyt(board):
		tbyt = [ board[j][i] for j in range(6,9) for i in range(3) ] # bottom left 3x3 matrix
		return result(tbyt)
		
	def midleft_tbyt(board):
		tbyt = [ board[j][i] for j in range(3,6) for i in range(3) ]# mid left 3x3 matrix
		return result(tbyt)
		
	def midtop_tbyt(board):
		tbyt = [ board[i][j] for j in range(3,6) for i in range(3) ]# mid top 3x3 matrix
		return result(tbyt)
		
	def topright_tbyt(board):
		tbyt = [ board[i][j] for j in range(6,9) for i in range(3) ]# top right 3x3 matrix
		return result(tbyt)

	def midright_tbyt(board):
		tbyt = [ board[j][i] for j in range(3,6) for i in range(6,9) ]# mid right 3x3 matrix
		return result(tbyt)

	def midbottom_tbyt(board):		
		tbyt = [ board[i][j] for j in range(3,6) for i in range(6,9) ]# mid bottom 3x3 matrix
		return result(tbyt)

	""" Function to check the repeating pattern of 3x3 matrix """			
	def result(test):
		if  str(test).count('1') and str(test).count('2') and str(test).count('3') and str(test).count('4') and str(test).count('5') and str(test).count('6') and str(test).count('7') and str(test).count('8') and str(test).count('9') < 2:
			return True
		else:
			return False	
	
	""" Function to check repeating pattern of numbers for all the ROWS """
	def ro(board):
		rs = []
		for i in range(9):
			rw = str(board[i])
		
			if str(rw).count(str(1)) and str(rw).count(str(2)) and str(rw).count(str(3)) and str(rw).count(str(4)) and str(rw).count(str(5)) and str(rw).count(str(6)) and str(rw).count(str(7)) and str(rw).count(str(8)) and str(rw).count(str(9)) < 2:
				rs.append(True)
			else:
				rs.append(False)
		# print("rows", rs)
		if False in rs:
			return False
		else:
			return True
	
	""" To count repeating pattern of numbers in COLUMNS """
	
	def co(board):
		colu = []
		test = [ [board[j][i] for j in range(9)] for i in range(9)]
		for i in range(9):
			col = str(test[i])
			
			if col.count(str(1)) and col.count(str(2)) and col.count(str(3)) and col.count(str(4)) and col.count(str(5)) and col.count(str(6)) and col.count(str(7)) and col.count(str(8)) and col.count(str(9)) < 2:
				colu.append(True)
			else:
				colu.append(False)
		# print("cols", colu)
		if False in colu:
			return False
		else:
			return True
	
	""" If the result from all the above functions is True then result is True else False """	
	
	if co(board) and ro(board) and midbottom_tbyt(board) and midright_tbyt(board) and topright_tbyt(board) and midtop_tbyt(board) and midleft_tbyt(board) and bleft_tbyt(board) and bright_tbyt(board) and center_tbyt(board) and first_tbyt(board) == True:
		return True
	else:
		return False
	
print(validSolution(tes))
