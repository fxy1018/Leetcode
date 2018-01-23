'''
Created on Jan 22, 2018

@author: XFan

Given a text txt[0..n-1] and a pattern pat[0..m-1], write a function search(char pat[], char txt[]) that prints all occurrences of pat[] in txt[]. You may assume that n > m.

Examples:

Input:  txt[] = "THIS IS A TEST TEXT"
        pat[] = "TEST"
Output: Pattern found at index 10

Input:  txt[] =  "AABAACAADAABAABA"
        pat[] =  "AABA"
Output: Pattern found at index 0
        Pattern found at index 9
        Pattern found at index 12
        
similar to LC28
'''

class Solution(object):
    #O(m*(n-m+1))
    def searchPattern1(self, txt, pat):
        if not txt or not pat:
            return(None)
        
        if len(pat) > len(txt):
            return(None)
        
        n = len(txt)
        m = len(pat)
        res = []
        for i in range(n-m+1):
            for j in range(m):
                if pat[j] != txt[i+j]:
                    break
            res.append(i)
        return(res)
    #KMP algorithm, O(N)
    def KMP(self, txt, pat):
        #http://www.matrix67.com/blog/archives/115
        #preprocessing the pat
        lps = self.getLPS(pat)
        n = len(txt)
        m = len(pat)
        
        i = 0
        j = 0
        res = []
        while i < n:
            if txt[i] == pat[j]:
                i += 1
                j += 1
                if j == m:
                    res.append(i-m)
                    j = lps[j-1]
            else:
                if j != 0:
                    j = lps[j-1]
                else:
                    i += 1 
        print(res)
        
        
    def getLPS(self, pat):
        lps = [0]
        m = len(pat)   
        for i in range(1, m):
            match = 0
            for j in range(i):
                if pat[:j+1] == pat[i-j : i+1]:
                    match = max(match, j+1)
                
            lps.append(match)
        return(lps)


s = Solution()
s.KMP("ABABDABACDABABCABAB", "ABABCABAB")
        
                
                
                
                
                
