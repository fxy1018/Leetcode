'''
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Time complexity : O(n)O(n). Time complexity is O(n)O(n) because accessing the counter table is a constant time operation.

Space complexity : O(1)O(1). Although we do use extra space, the space complexity is O(1)O(1) because the table's size stays constant no matter how large nn is.
'''

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        sHash = {}
        for char in s:
            sHash[char] = sHash.get(char, 0) + 1
        
        for char in t:
            if char not in sHash:
                return(False)
            if sHash[char]-1 < 0:
                return(False)
            sHash[char] = sHash[char] - 1
        
        
        for key in sHash:
            if sHash[key] > 0:
                return(False)
        return(True)
