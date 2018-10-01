"""

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example,
Given board =

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.

"""
'''
Created on Feb 9, 2017

@author: fanxueyi
'''

class Solution(object):
    def __init__(self):
        self.row = 0
        self.col = 0
        self.visited = []
        
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return(False)
            
        self.row = len(board)
        self.col = len(board[0])
        self.visited = [[False]*self.col for i in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                if (self.helpFun(board, word, i, j , 0)):
                    return(True)
        return(False)
        
    def helpFun(self, board, word, i, j, index):
        if index == len(word):
            return(True)
        
        if (i<0 or j<0 or i >= self.row or j>=self.col):
            return(False)
            
        if (self.visited[i][j]):
            return(False)
            
        if board[i][j] != word[index]:
            return(False)
        
        self.visited[i][j] = True
        
        #left letter:
        if self.helpFun(board, word, i, j-1, index+1):
            return(True)
        #right letter:
        if self.helpFun(board, word, i, j+1, index+1):
            return(True)
        #up letter:
        if self.helpFun(board, word, i-1, j, index+1):
            return(True)
        #down letter:
        if self.helpFun(board, word, i+1, j, index+1):
            return(True)
        
        self.visited[i][j] = False
        return(False)
        
            
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
    
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board or not word:
            return(False)
        
        row = len(board)
        col = len(board[0])
        
        if row*col < len(word):
            return(False)
        #dfs
        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    visit = set([])
                    visit.add((i,j))
                    if self.dfs(board, i, j, word[1:], visit):
                        return(True)
        return(False)
    
    def dfs(self, board, x, y, word,visit):
        if not word:
            return(True)
        
        if x > 0 and (x-1,y) not in visit and board[x-1][y] == word[0]:
            visit.add((x-1, y))
            if self.dfs(board,x-1,y, word[1:], visit):
                return(True)
            visit.remove((x-1,y))
        
        if y > 0 and (x,y-1) not in visit and board[x][y-1] == word[0]:
            visit.add((x, y-1))
            if self.dfs(board,x,y-1, word[1:], visit):
                return(True)
            visit.remove((x,y-1))   
        
        if x < len(board)-1 and (x+1,y) not in visit and board[x+1][y] == word[0]:
            visit.add((x+1, y))
            if self.dfs(board,x+1,y, word[1:], visit):
                return(True)
            visit.remove((x+1,y))
        
        if y < len(board[0])-1 and (x,y+1) not in visit and board[x][y+1] == word[0]:
            visit.add((x, y+1))
            if self.dfs(board,x,y+1, word[1:], visit):
                return(True)
            visit.remove((x,y+1))   
        
        return(False)            
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return(False)
        
        m = len(board)
        n = len(board[0])
        visited = [[False for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if self.helpFun(board, word, i, j, visited):
                    return(True)
        return(False)
        
        
    def helpFun(self, board, word, i, j, visited):
        if not word:
            return(True)
        
        if i<0 or j<0 or i>=len(board) or j >= len(board[0]):
            return(False)
        
        if visited[i][j]:
            return(False)
        
        if (board[i][j] != word[0]):
            return(False)
        
        visited[i][j] = True
     
        if self.helpFun(board, word[1:], i-1, j, visited):
            return(True)
        
        if self.helpFun(board, word[1:], i, j-1, visited):
            return(True)
        
        if self.helpFun(board, word[1:], i+1, j, visited):
            return(True)
        
        if self.helpFun(board, word[1:], i, j+1, visited):
            return(True)
        visited[i][j] = False
        return(False)
