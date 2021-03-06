"""

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

For "(()", the longest valid parentheses substring is "()", which has length = 2.

Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

"""

'''
Created on Feb 17, 2017

@author: fanxueyi
'''

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        #stack
        n = len(s)
        stack = []
        max_len = 0
        curr_len = 0 
        
        for i in range(n):
            if s[i] == "(":
                stack.append((i,0))
            else:
                if not stack or stack[-1][1] == 1:
                    stack.append((i,1))
                else:
                    stack.pop()
                    if not stack:
                        curr_len = i+1
                    else:
                        curr_len = i-stack[-1][0]
                    max_len = max(max_len, curr_len) 
        return max_len
 class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        #DP
        if not s:
            return(0)
        dp = [0] * len(s)
        for i in range(1, len(s)):
            pre = i-dp[i-1] -1
            if s[i] == ")" and pre>=0 and s[pre] == "(":
                if pre > 0:
                    dp[i] = dp[i-1] + 2 + dp[pre-1]
                else:
                    dp[i] = dp[i-1] + 2      
        return(max(dp))
            
