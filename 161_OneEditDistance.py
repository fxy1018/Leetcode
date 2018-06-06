'''
Given two strings S and T, determine if they are both one edit distance apart.

Example
Given s = "aDb", t = "adb"
return true

edit: insert, delete, replace

'''
class Solution:
    """
    @param s: a string
    @param t: a string
    @return: true if they are both one edit distance apart or false
    """
    def isOneEditDistance(self, s, t):
        # write your code here
        n = len(s)
        m = len(t)
        if abs(n-m) > 1:
            return(False)
        
        misCount = 0
        if n == m:
            for i in range(n):
                if s[i] != t[i]: 
                    if misCount<1:
                        misCount += 1
                    else:
                        return(False)
            return(misCount == 1)
            
        elif n > m:
            for i in range(n):
                tmp = s[:i] + s[i+1:]
                if tmp == t:
                    return(True)
            return(False)
        else:
            for i in range(m):
                tmp = t[:i] + t[i+1:]
                if tmp == s:
                    return(True)
            return(False)
                
            
