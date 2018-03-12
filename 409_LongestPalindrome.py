'''

Given a string which consists of lowercase or uppercase letters, find the length of the longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.

Example:

Input:
"abccccdd"

Output:
7

Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.

'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        singleChar = 0
        sHash = {}
        for char in s:
            sHash[char] = sHash.get(char, 0) + 1
            
        for key in sHash:
            if sHash[key] %2 ==0:
                res += sHash[key]
            elif sHash[key] > 1:
                res += sHash[key]-1
                singleChar = 1
            else:
                singleChar = 1
        
        return(res+singleChar)
        
 class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        res = 0
        sHash = {}
        for char in s:
            sHash[char] = sHash.get(char, 0) + 1
            if sHash[char] == 2:
                res += 2
                sHash[char] = 0
        for key in sHash:
            if sHash[key] == 1:
                return(res+1)
        return(res)
