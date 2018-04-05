"""
"""
"""

1) Start in the leftmost column
2) If all queens are placed
    return true
3) Try all rows in the current column.  Do following for every tried row.
    a) If the queen can be placed safely in this row then mark this [row, 
        column] as part of the solution and recursively check if placing  
        queen here leads to a solution.
    b) If placing queen in [row, column] leads to a solution then return 
        true.
    c) If placing queen doesn't lead to a solution then umark this [row, 
        column] (Backtrack) and go to step (a) to try other rows.
3) If all rows have been tried and nothing worked, return false to trigger 
    backtracking.

"""



'''
Created on Jan 21, 2017

@author: fanxueyi
'''
class Solution(object):    
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        self.field = [["." for j in range(n)] for i in range(n)]
        self.n = n
        self.res=[]
        self.NQueens(0)
        return(self.res)
        
    def NQueens(self, col):
        if col==self.n:
            self.res.append(["".join(j) for j in self.field])
            return
            
        for row in range(self.n):
            if not self.isCollision(row,col):
                self.field[row][col]="Q"
                self.NQueens(col+1)   
                self.field[row][col]="."
      
    def isCollision(self, row , col):
        #check row and colomn
        for c in range(self.n):
            if self.field[row][c]=="Q":
                return(True)
        for r in range(self.n):
            if self.field[r][col]=="Q":
                return(True)
        #check diagnal
        row_up = row-1
        row_down= row+1
        col = col-1
        while col>=0:
            if row_up >=0:
                if (self.field[row_up][col]=="Q"):
                    return(True)
            if row_down <self.n:
                if (self.field[row_down][col]=="Q"):
                    return(True)
        
            row_up -=1
            row_down +=1
            col -=1
        
        return(False)
    
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        curr = [["."] * n  for _ in range(n)]
        self._helpFun(res, n, 0, curr)
        return(res)
           
    def _helpFun(self, res, n, index, curr):
        if index == n:
            res.append(["".join(i) for i in curr])
            return
        for j in range(n):
            if self._isAttatched(index, j, curr, n):
                continue
            else:
                curr[index][j] = "Q"
                self._helpFun(res, n, index+1, curr)
                curr[index][j] = "."
        return

    def _isAttatched(self, rowIndex, colIndex, curr, n):
        #check column
        for i in range(rowIndex):
            if curr[i][colIndex] == "Q":
                return(True)
        
        #check diagnal
        for i in range(rowIndex):
            for j in range(n):
                if curr[i][j] == "Q" and abs(rowIndex-i) == abs(colIndex-j):
                    return(True)
        return(False)
                
    
    
        
        
        
s = Solution()
print(s.solveNQueens(4))
