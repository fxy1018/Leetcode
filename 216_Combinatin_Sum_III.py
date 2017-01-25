"""
Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Example 1:

Input: k = 3, n = 7

Output:

[[1,2,4]]

Example 2:

Input: k = 3, n = 9

Output:

[[1,2,6], [1,3,5], [2,3,4]]

"""

'''
Created on Jan 24, 2017

@author: fanxueyi
'''


class Solution(object):
    def __init__(self):
        self.result = []
        self.k = 0
        self.n = 0
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        self.k = k 
        self.n = n 
        candidates = [1,2,3,4,5,6,7,8,9]
        comb=[]
        self.helpFun(0, 0, n, comb, candidates)
        return(self.result)
    
    def helpFun(self, index,count, target, comb,candidates):
        comb.sort()
        if count == self.k and sum(comb) == self.n and comb not in self.result:
            self.result.append(comb)
            return
        
        for i in range(index,len(candidates)):
            tmp_target = target-candidates[i]
            if tmp_target>=0:
                new_comb = comb + [candidates[i]]
                self.helpFun(i+1, count+1, tmp_target, new_comb, candidates)
            
        
        



