'''
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example
Given board =

[
  "ABCE",
  "SFCS",
  "ADEE"
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.


Time: m*n*4^(k-1)
'''

class Solution:
    """
    @param board: A list of lists of character
    @param word: A string
    @return: A boolean
    """
    def exist(self, board, word):
        # write your code here
        if not board or not word:
            return(False)
            
        board = [list(w) for w in board]
        visited = set({})
        curr = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    visited.add((i,j))
                    if self.helpFun(board, word, visited, 1, i, j):
                        return(True)
                    visited.remove((i,j))
        return(False)
    
    def helpFun(self, board, word, visited, curr, x, y):
        if curr == len(word):
            return(True)
        
        target = word[curr]
        
        if x >0 and (x-1, y) not in visited and board[x-1][y] == target:
            visited.add((x-1,y))
            if self.helpFun(board, word, visited, curr+1, x-1, y):
                return(True)
            else:
                visited.remove((x-1,y))
                
        if y >0 and (x, y-1) not in visited and board[x][y-1] == target:
            visited.add((x,y-1))
            if self.helpFun(board, word, visited, curr+1, x, y-1):
                return(True)
            else:
                visited.remove((x,y-1))
            
        if x < len(board)-1 and (x+1, y) not in visited and board[x+1][y] == target:
            visited.add((x+1,y))
            if self.helpFun(board, word, visited, curr+1, x+1, y):
                return(True)
            else:
                visited.remove((x+1,y))
                
        if y < len(board[0])-1 and (x, y+1) not in visited and board[x][y+1] == target:
            visited.add((x,y+1))
            if self.helpFun(board, word, visited, curr+1, x, y+1):
                return(True)
            else:
                visited.remove((x,y+1))
                
        return(False)
        
        
        
