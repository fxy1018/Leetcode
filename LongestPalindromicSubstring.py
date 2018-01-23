'''
Created on Jan 23, 2018

@author: XFan

Given a string, find the longest substring which is palindrome.

if the given string is "forgeeksskeegfor", the output should be "geeksskeeg"
if the given string is "abaaba", the output should be "abaaba"
if the given string is "abababa", the output should be "abababa"
if the given string is "abcbabcbabcba", the output should be "abcbabcba"

LC:5
'''

class Solution(object):
    
    #brute-force, time:O(n^3), space: O(1)
    def LongestPalindromicSubstring(self, txt):
        if not txt:
            return("")
        out = ""
        length = 0
        for i in range(len(txt)):
            for j in range(i+1, len(txt)+1):
                tmp = txt[i:j]
                if tmp == tmp[::-1] and (j-i) > length:
                        length = j-i
                        out = txt[i:j]
        return(out)
    
    
    #DP, time: O(n^2), space: O(n^2)
    def LongestPalindromicSubstring2(self, txt):
        if not txt:
            return("")
        n = len(txt)
        if n == 1:
            return(txt)
        if n == 2:
            if txt[0] == txt[1]:
                return(txt)
            else:
                return(txt[0])

        dp = [[False for _ in range(n)] for _ in range(n)]
        out = txt[0]
        length = 1
        for i in range(n):
            dp[i][i] = True
        
        for i in range(n-1):
            dp[i][i+1] = (txt[i] == txt[i+1])
            if dp[i][i+1]:
                out = txt[i:i+2]
                length = 2
        
        for j in range(2, n):
            for i in range(0, j-1):
                dp[i][j] = (dp[i+1][j-1] and txt[i] == txt[j])
                if dp[i][j] and j-i+1 > length:
                    length = j- i + 1
                    out = txt[i:(j+1)]
        return(out)
    
    #expand around center, odd and even str,time: O(n^2), space: O(1)
    def LongestPalindromicSubstring3(self, txt):
        if not txt:
            return("")
        n = len(txt)
    #manacher, time: O(n^2)
    def LongestPalindromicSubstring4(self, txt):
        
                    
txt = "abcba"
s = Solution()
print(s.LongestPalindromicSubstring2(txt))
        
            
        
        
        
        
