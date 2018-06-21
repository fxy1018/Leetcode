'''

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input: 
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output: 
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?
'''


class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        
        #use another one to record 
        row = len(board)
        col = len(board[0])
        newBoard = [[0]*col for _ in range(row)]
        
        for i in range(row):
            for j in range(col):
                newBoard[i][j] = self.getState(board, i, j)
        for i in range(row):
            for j in range(col):
                board[i][j] = newBoard[i][j]
        return
    
    def getState(self, board, i, j):
        num1 = 0
        if i > 0 and j > 0:
            num1 += board[i-1][j-1]==1
            
        if i > 0:
            num1 += board[i-1][j]==1
            
        if i > 0 and j < len(board[0])-1:
            num1 += board[i-1][j+1]==1
        
        if j>0:
            num1 += board[i][j-1]==1
        
        if j < len(board[0])-1:
            num1 += board[i][j+1]==1
            
        if i < len(board)-1 and j > 0:
            num1 += board[i+1][j-1]==1
            
        if i < len(board)-1:
            num1 += board[i+1][j]==1
            
        if i < len(board)-1 and j < len(board[0])-1:
            num1 += board[i+1][j+1]==1
        
        if board[i][j] == 1 and (num1<2 or num1>3):
            return(0)
        
        if board[i][j] == 1 and (num1==2 or num1==3) :
            return(1)
        
        if board[i][j] == 0 and num1 == 3:
            return(1)
        else:
            return(0)
            

        
        
        
