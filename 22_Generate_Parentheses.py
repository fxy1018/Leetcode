"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

"""


'''
Created on Jan 22, 2017

@author: fanxueyi
'''

class Solution(object):
    def __init__(self):
        self.result=[]
        self.n=0
        self.created = []
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.n = n
        comb=""
        self.helpFun(comb,0)
        return(self.result)
        
        
    def helpFun(self,comb,count):
        if count == self.n:
            self.result.append(comb)
            return
        for i in range(len(comb)+1):
            if i == 0:
                comb_new = "()"+comb
            elif i == len(comb):
                comb_new = comb+"()"
            else:
                comb_new = comb[0:i]+"()"+comb[i:] 
            if comb_new not in self.created:
                self.created.append(comb_new)
                self.helpFun(comb_new,count+1)