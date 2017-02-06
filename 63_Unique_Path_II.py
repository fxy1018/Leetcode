"""
Follow up for "Unique Paths":

Now consider if some obstacles are added to the grids. How many unique paths would there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

For example,
There is one obstacle in the middle of a 3x3 grid as illustrated below.

[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
The total number of unique paths is 2.

Note: m and n will be at most 100.

"""
'''
Created on Feb 6, 2017

@author: fanxueyi
'''
class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        
        #method1: dynamic programming
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[0]*n for i in range(m)]
        
        for i in range(n):
            if obstacleGrid[0][i]==1:
                dp[0][i]=0
                break
            else:
                dp[0][i]=1
        
        for j in range(m):
            if obstacleGrid[j][0]==1:
                dp[j][0]=0
                break
            else:
                dp[j][0]=1
                
                
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    continue
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return(dp[m-1][n-1])
             
            
        