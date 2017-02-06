"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?

"""


'''
Created on Feb 6, 2017

@author: fanxueyi
'''
class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        """
        #method1:math, combination problem
        steps = m+n-2
        out = self.factorial(steps)/(self.factorial(m-1)*self.factorial(steps-m+1))
        return(out)
    
    def factorial(self, n):
        res = 1
        for i in range(1, n+1):
            res *= i
        return(res)
        """
        
        #这道题就是一个动态规划，所以每一个位置的走法数量，就是其左边和上方的和。 
        #因为只能右边和下方走，那么对于每一个格子，其就只可能来自这两个方向，那么其往某个格子过来，就正好带来对应的解法，这里一共有两个，所以就是他们的和
        #method2: dynamic programming
        dp = [[0]*n for i in range(m)]
        for i in range(n):
            dp[0][i]=1
        for j in range(m):
            dp[j][0]=1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i][j-1] + dp[i-1][j]
                
        return(dp[m-1][n-1])
        
