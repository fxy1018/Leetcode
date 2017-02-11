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
        
            
            
    
            