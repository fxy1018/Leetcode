'''

Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Here is an example:
S = "rabbbit", T = "rabbit"

Return 3.


'''

class Solution(object):
    #memorization
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        if not s and not t:
            return(1)
        if not s:
            return(0)
        dp = [[-1]*(len(t)+1) for i in range(len(s)+1)]
        
        res = self.helpFun(0,0,s,t, dp)
        return(res)

    def helpFun(self, m, n, s, t,dp):
        if n ==len(t):
            dp[m][n] = 1
            return(1)
        if m == len(s):
            dp[m][n] = 0
            return(0)
            
        if dp[m][n] != -1:
            return(dp[m][n])

        tmp=0
        for i in range(m, len(s)):
            if s[i] == t[n]: 
                tmp += self.helpFun(i+1, n+1, s, t, dp)
                 
        dp[m][n] = tmp
        return(dp[m][n])
