"""

Given a string, find the length of the longest substring T that contains at most 2 distinct characters.

For example, Given s = "eceba"
T is "ece" which its length is 3.

"""


'''
Created on Feb 18, 2017

@author: fanxueyi
'''

class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = max_len = count = 0
        char_hash = {}
        
        for i in range(len(s)):
            if s[i] not in char_hash:
                count += 1
                char_hash[s[i]] = i
            if count <3:
                max_len = max(max_len, i-start+1)
            if count > 2:
                max_len = max(max_len, i-start)
                done = True
                char = s[i-1]
                index = i-1
                while done:
                    if s[index] == char:
                        index -= 1
                    else:
                        done = False
                start = index + 1
                char_hash={s[i]:i, s[start]:start}
                count = 2
        return(max_len)
    #modified code:
    def lengthOfLongestSubstringTwoDistinct2(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = max_len = count = 0
        char_hash = {}
        
        for i in range(len(s)):
            if s[i] not in char_hash:
                count += 1
            char_hash[s[i]] = i
            if count <3:
                max_len = max(max_len, i-start+1)
            if count > 2:
                max_len = max(max_len, i-start)
                count = 2
                start = min(char_hash.values())+1
                char_hash.pop(s[start-1])
        return(max_len)

    def longestSubstring3(self, s, k):
        start = max_len = 0
        s_hash  = {}
        for i in range(len(s)):
            s_hash [s[i]] = i
            if len(s_hash) < 3:
                max_len = max(max_len, i-start+1)
            
            else:
                max_len = max(max_len, i-start)
                start = min(s_hash.values())+1
                s_hash.pop(s[start-1])
        return(max_len)
                

    
s= Solution()
print(s.lengthOfLongestSubstringTwoDistinct2("ba"))
print(s.longestSubstring3("ba", 2))