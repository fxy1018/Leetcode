'''
Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t
To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

Example 1:

Input: s1 = "great", s2 = "rgeat"
Output: true
Example 2:

Input: s1 = "abcde", s2 = "caebd"
Output: false

'''

class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)
        if l1 != l2:
            return(False)
        return(self.helpFun(0, l1-1, 0, l2-1, s1,s2) or self.helpFun(0, l1-1, l2-1, 0, s1, s2))
    
    def helpFun(self, start1, end1, start2, end2, s1, s2):
        
        if start1 == end1:
            return(s1[start1] == s2[start2])
        
        res = False
        for i in range(start1, end1+1):
            currStr1 = s1[start1:(i+1)]
            currStr2 = s2[start2:(start2+ (i-start1)+1)]
            currStr3 = s2[end2-(i-start1):end2+1]
            if self.isSame(currStr1, currStr2):
                res = res or (self.helpFun(start1, i, start2, start2+(i-start1), s1, s2) and self.helpFun(i+1, end1, start2+(i-start1)+1, end2, s1, s2))
            if self.isSame(currStr1, currStr3):
                res = res or (self.helpFun(start1, i, end2-(i-start1)+1, end2, s1, s2) and self.helpFun(i+1, end1, start2, end2-(i-start1), s1, s2))
        
        return(res)
    
    def isSame(self, str1, str2):
        return(sorted(str1)==sorted(str2))
 
 time: O(n^4), space: O(n^4)
 class Solution(object):
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l1 = len(s1)
        l2 = len(s2)
        if l1 != l2 or not s1 or not s2:
            return(False)
        if s1==s2:
            return(True)
        
        if sorted(s1) != sorted(s2):
            return(False)
        
        for i in range(1, l1):
            s11 = s1[:i]
            s12 = s1[i:]
            s21 = s2[:i]
            s22 = s2[i:]
            
            if self.isScramble(s11, s21) and self.isScramble(s12, s22):
                return(True)
            s21 = s2[:l2-i]
            s22 = s2[l2-i:]
            if self.isScramble(s11, s22) and self.isScramble(s12, s21):
                return(True)
        
        return(False)     
   
