'''
Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters, and str contains lowercase letters separated by a single space.

'''

class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        
        patternHash = {}
        strHash = {}
        strArray = str.split(" ")
        if len(pattern) != len(strArray):
            return(False)
        
        pair = zip(pattern, strArray)
        for p in pair:
            if p[0] not in patternHash:
                patternHash[p[0]] = p[1]
            if p[1] not in strHash:
                strHash[p[1]] = p[0]
            if patternHash[p[0]] != p[1]:
                return(False)
            if strHash[p[1]] != p[0]:
                return(False)
        return(True)
            
