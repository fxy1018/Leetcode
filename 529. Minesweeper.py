class Solution(object):
	def updateBoard(self, board, click):
		"""
		:type board: List[List[str]]
		:type click: List[int]
		:rtype: List[List[str]]
		"""
		row = len(board)
		col = len(board[0])
		queue = [(click[0], click[1])]
		visited = set((click[0], click[1]))
		while queue:
			x,y = queue.pop(0)
			if board[x][y] == "M":
				board[x][y] = "X"
			else:
				neighbors = self.getNeighbors(board, x, y, row, col)
				mineNumber = sum(board[nr][nc] in "M" for nr, nc in neighbors) 
				if mineNumber>0:
					board[x][y] = str(mineNumber)
				else:
					board[x][y] = "B"
					for n_x, n_y in neighbors:
						if (n_x, n_y) not in visited and board[n_x][n_y] in "BE":
							queue.append((n_x,n_y))
							visited.add((n_x,n_y))
		return(board)

	def getNeighbors(self,board, x, y , row, col):
		res =[]
		for dr in xrange(-1, 2):
			for dc in xrange(-1, 2):
				if (dr or dc) and 0 <= x + dr < row and 0 <= y + dc < col:
					res.append((x + dr, y + dc))
		return(res)
