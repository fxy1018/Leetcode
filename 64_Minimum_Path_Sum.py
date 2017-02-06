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
            #print(dp[i][0])
        
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
            #print(grid[0][j-1],grid[0][j],dp[0][j])
        
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i-1][j], dp[j-1][i])+grid[i][j]
         
        #print(dp)   
        return(dp[m-1][n-1])
    
s =Solution()
print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1]]))
            
            
            
            