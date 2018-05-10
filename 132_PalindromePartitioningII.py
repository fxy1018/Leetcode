'''
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:

Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

'''
class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        #use p to record head string palindrome p[i][j] means from i to j, whether the substring is palindrome
        l = len(s)
        p = [[False] * l for _ in range(l)]
        memo = [0] * l
        p[l-1][l-1] = True
        for i in range(l-1):
            p[i][i] = True
            p[i][i+1] = s[i] == s[i+1]
            
        for z in range(2, l):
            for i in range(l-z):
                if s[i] == s[i+z]:
                    p[i][i+z] = p[i+1][i+z-1]   
                        
        return(self.helpFun(0, s, p, memo)-1)
    
    def helpFun(self, pos, s, p, memo):
        if pos == len(s):
            return(0)
        if memo[pos] != 0:
            return(memo[pos])
        res = len(s) - pos
        for i in range(pos, len(s)):
            if p[pos][i]:
                res = min(res, self.helpFun(i+1,s,p, memo))
        
        memo[pos] = res + 1
        return(memo[pos])

