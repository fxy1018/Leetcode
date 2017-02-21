"""

Given a string, find the length of the longest substring T that contains at most k distinct characters.

For example, Given s = “eceba” and k = 2,

T is "ece" which its length is 3.


"""
'''
Created on Feb 18, 2017

@author: fanxueyi
'''
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        start = max_len = count = 0
        char_hash = {}
        
        for i in range(len(s)):
            if s[i] not in char_hash:
                count += 1
            char_hash[s[i]] = i
            if count <= k:
                max_len = max(max_len, i-start+1)
            if count > k:
                max_len = max(max_len, i-start)
                count = k
                start = min(char_hash.values())+1
                char_hash.pop(s[start-1])
        return(max_len)
                
        
        