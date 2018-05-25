"""

Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

"""

'''
Created on Mar 12, 2017

@author: fanxueyi
'''

#DP, bottom up

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0 for i in range(n + 1)] 
        
        dp[0] = 1
        dp[1] = 1
        
        if n >= 2:
            for i in range(2, n+1):
                for j in range(0, i):
                    dp[i] += dp[j] * dp[i-1-j]
        
        return(dp[n])
    
    
    
    #modified 
    def numTrees2(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 1
        
        dp = [0 for i in range(n + 1)] 
        dp[0] = 1
        
        for i in range(1, n+1):
            for j in range(0, i):
                dp[i] += dp[j] * dp[i-1-j]
        
        return(dp[n])
class Solution:
    """
    @param n: An integer
    @return: An integer
    """
    def numTrees(self, n):
        # write your code here
        if n == 0:
            return(1)
        dp = [0] * (n+1)
        dp[0] = 1
        dp[1] = 1 
        
        for i in range(2, n+1):
            tmp = 0
            for j in range(1, i+1):
                small = j - 1
                large = i - j
                tmp += dp[j-1] * dp[i-j]
            dp[i] = tmp
        return(dp[-1])
        
