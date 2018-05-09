'''

Validate if a given string is numeric.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true

Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

Update (2015-02-10):
The signature of the C++ function had been updated. If you still see your function signature accepts a const char * argument, please click the reload button to reset your code definition.
'''

#https://blog.csdn.net/sjt19910311/article/details/46648283
# not working in Leetcode 
class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = s.strip(" ")
        if not s:
            return(False)
        res = ""
        dotN = 0
        eN = 0
        nN = 0
        for i in range(len(s)):
            c = s[i]
            if (i == 0 and c == "e"):
                return(False)
            if (c == "e" and i == len(s)-1):
                return(False)
            if c == "e":
                eN += 1
                if eN > 1:
                    return(False)
                
            if c == " " or (c.isalpha() and c != "e"):
                return(False)
            if c == ".":
                dotN += 1
                if dotN > 1:
                    return(False)
            if c in "0123456789":
                nN += 1
            res += c
        if nN == 0:
            return(False)
        if ".e" in res or "e." in res:
            return(False)
        
        
        return(True)
                
#regular expression
import re
class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        regex = '^\s*[+|-]?(\d+\.?\d*|\d*\.?\d+)(e[+|-]?\d+)?\s*$'
        if not re.match(regex, s):
            return(False)
        else:
            return(True)
                    
            
            
        
