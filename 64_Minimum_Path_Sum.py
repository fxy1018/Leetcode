"""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

"""
'''
Created on Feb 6, 2017

@author: fanxueyi
'''

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[0]*n for i in range(m)]
        
        dp[0][0] = grid[0][0]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
        
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j], dp[j-1][i])+grid[i][j]
  
        return(dp[m-1][n-1])
    
    #空间压缩， one arrays
    def minPathSum2(self,grid):
        if not grid:
            return(0)
            
        m = len(grid)
        n = len(grid[0])
        dp1 = [0] * n
        dp2 = [0] * n
        
        dp1[0] = grid[0][0]
        
        for i in range(1,n):
            dp1[i] = dp1[i-1] + grid[0][i]
        
        for i in range(1,m):
            for j in range(0,n):
                if j == 0:
                    dp2[j] = dp1[j] + grid[i][j]
                else: 
                    dp2[j] = min(dp1[j], dp2[j-1])+grid[i][j]
            dp1 = dp2
        return(dp1[-1])
    
    #空间压缩， one arrays
    def minPathSum3(self,grid):
        if not grid:
            return(0)
            
        m = len(grid)
        n = len(grid[0])
        dp = [0] * n

        
        dp[0] = grid[0][0]
        
        for i in range(1,n):
            dp[i] = dp[i-1] + grid[0][i]
    
        for i in range(1,m):
            for j in range(0,n):
                if j == 0:
                    dp[j] = dp[j] + grid[i][j]
                else: 
                    dp[j] = min(dp[j], dp[j-1])+grid[i][j]

        return(dp[-1])
        
        
s =Solution()
print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
            
            
            
            