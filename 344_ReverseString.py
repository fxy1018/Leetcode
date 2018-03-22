'''

Write a function that takes a string as input and returns the string reversed.

Example:
Given s = "hello", return "olleh".


'''

class Solution:
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        #method1:
        return(s[::-1])
        
        #method2:
        l = len(s)-1
        res = ""
        for j in range(l, -1, -1):
            res+=s[j]
            
        return(res)
