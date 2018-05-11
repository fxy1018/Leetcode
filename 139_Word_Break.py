"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words. You may assume the dictionary does not contain duplicate words.

For example, given
s = "leetcode",
dict = ["leet", "code"].

Return true because "leetcode" can be segmented as "leet code".

"""
'''
Created on Feb 28, 2017

@author: fanxueyi
'''

class Solution(object):
    #time limit exceeded
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        if not s or not wordDict:
            return False
        if len(s) == 1:
            if s in wordDict:
                return True
            else:
                return False
        return self.helpFun(s, wordDict)

    def helpFun(self, s, wordDict):
        if s in wordDict:
            return True
        for i in range(1,len(s)):
            if s[:i] in wordDict and self.wordBreak(s[i:], wordDict):
                return True
        
        return False
    
    #DP to solve
    def wordBreak2(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        
        for i in range(1,len(s)+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return(dp[-1])
    
    
    class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordSet = set(wordDict)
        l = len(s)
        dp = [False] * (l+1)
        dp[0] = True
        dp[1] = True if s[0] in wordSet else False
        
        for i in range(1, l):
            for j in range(0, i+1):
                if s[j:i+1] in wordSet and dp[j]:
                    dp[i+1] = True
                    break
        return(dp[-1])
class Solution:
    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        wordDict = set(wordDict)
        dp = [False for i in range(len(s)+1)]
        dp[0] = True
        
        for i in range(1,len(s)+1):
            for j in range(0, i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return(dp[-1])
