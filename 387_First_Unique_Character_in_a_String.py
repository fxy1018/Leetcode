"""

Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.

"""

'''
Created on Feb 20, 2017

@author: fanxueyi
'''

class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        s_hash = {}
        
        for i in range(len(s)):
            if s[i] in s_hash:
                s_hash[s[i]][0] +=1
            else:
                s_hash[s[i]] = [1, i]
        index = float("Inf")
        for key in s_hash:
            if s_hash[key][0] <2:
                index = min(index, s_hash[key][1])
        return(index if index < float("Inf") else -1)