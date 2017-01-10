#Given a string s, find the longest palindromic substring in s. 
#You may assume that the maximum length of s is 1000.

'''
Created on Jan 8, 2017

@author: fanxueyi
'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        #use Dynamic Programming Strategy
        n = len(s)
        max_len = 1
        start = 0
        palindrome = [[''] * n for i in range(n)]
        
        for i in range(n):
            palindrome[i][i] = True
        
        for i in range(n-1):
            if s[i] == s[i+1]:
                palindrome[i][i+1] =True
                start = i
                max_len = 2
            
        for curr_len in range(3,n+1):
            for i in range(n-curr_len+1):
                j = i+curr_len-1
                if (s[i] == s[j]) and palindrome[i+1][j-1]:
                    palindrome[i][j] = True
                    start = i
                    max_len = curr_len
            
        return(s[start:start+max_len])
                    
        