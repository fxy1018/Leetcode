"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

For example,
"A man, a plan, a canal: Panama" is a palindrome.
"race a car" is not a palindrome.

Note:
Have you consider that the string might be empty? This is a good question to ask during an interview.

For the purpose of this problem, we define empty string as valid palindrome.

"""


'''
Created on Mar 2, 2017

@author: fanxueyi
'''

import re

class Solution(object):
    #built-in string function
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return(True)
        
        new_s = "".join(i.lower for i in s if i.isalnum())
     
        if new_s == new_s[::-1]:
            return(True)
        else:
            return(False)
        
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) == 0:
            return(True)   
        
        new_s = re.sub("[^A-Za-z0-9]", "", s)
        
        return(s==s[::-1])
            
        