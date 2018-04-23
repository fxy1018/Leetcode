'''
Created on Feb 1, 2017

@author: fanxueyi
'''

"""
思路: 题意说的是不能有超过连续两个相同的颜色, 也就是说最多有两个相邻柱子染同样颜色.

所以在染一个柱子的时候, 要考虑是否和上一个柱子颜色相同. 

如果和上一个相同的话那么上一个有多少种和上上次不同的染色方案, 那么当前柱子也有多少种染色方案.

如果和上一个不同的话那么染色方案就为(k-1)*(之前总共多少染色方案).

"""

class Solution:
    """
    @param n: non-negative integer, n posts
    @param k: non-negative integer, k colors
    @return: an integer, the total number of ways
    """
    #dp[n][k] = dp[n-2]*(k-1) + dp[n-1] * (k-1)
    def numWays(self, n, k):
        # write your code here
        if n == 0 or k == 0:
            return(0)
        if n == 1:
            return(k)
        if n == 2:
            return(k*k)
        dp = [0 for _ in range(n)]
        dp[0] = k
        dp[1] = k *k
        for i in range(2, n):
            dp[i] = (k-1) * (dp[i-2] + dp[i-1]) 
        return(dp[-1])
        
        
