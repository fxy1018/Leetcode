"""

Implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "*") → true
isMatch("aa", "a*") → true
isMatch("ab", "?*") → true
isMatch("aab", "c*a*b") → false

"""

'''
Created on Feb 18, 2017

@author: fanxueyi
'''
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        #create DP matrix
        row, col = len(s)+1, len(p)+1
        DP = [[""] * col for i in range(row)]
        
        #initilize DP matrix
        DP[0][0] = True
        
        for j in range(1, col):
            if j == 1:
                if p[0] == "*":
                    DP[0][j] = True
                else:
                    DP[0][j] = False
            else:
                if p[j-1] != "*":
                    DP[0][j] = False
                else:
                    DP[0][j] = DP[0][j-1]
        for i in range(1, row):
            DP[i][0] = False
        
        #DP process
        for i in range(1, row):
            for j in range(1,col):
                if p[j-1] == "?" or p[j-1] == s[i-1]:
                    DP[i][j] = DP[i-1][j-1]
                elif p[j-1] == "*":
                    DP[i][j] = DP[i-1][j] or DP[i][j-1]
                else:
                    DP[i][j] = False
        return(DP[-1][-1])
        
        
        
        
        
        
        
        
        
        
        