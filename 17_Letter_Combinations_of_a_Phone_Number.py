"""
Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].


"""
'''
Created on Jan 21, 2017

@author: fanxueyi
'''

class Solution(object):
    def __init__(self):
        self.numdict = {'0':" ", "1":"",
                        '2':"abc", '3':"def", '4':"ghi", 
                        '5':"jkl",'6':"mno","7":"pqrs",
                        '8':"tuv",'9':"wxyz"}
        
        self.result =[]
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        self.n = len(digits)
        if self.n==0:
            return([])
        comb = ""
        self.helpFun(digits,0, comb)
        return(self.result)
     
    def helpFun(self, digits, index, comb):
        if index == len(digits):
            self.result.append(comb)
            return
        
        letters = self.numdict[digits[index]]
        for i in range(len(letters)):
            comb_new = comb + letters[i]
            self.helpFun(digits, index+1, comb_new)
                
            
        
        
        
        
        
            
        
        
        
        
        
        