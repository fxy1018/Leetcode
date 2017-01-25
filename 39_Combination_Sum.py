"""
Given a set of candidate numbers (C) (without duplicates) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

The same repeated number may be chosen from C unlimited number of times.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [2, 3, 6, 7] and target 7, 
A solution set is: 
[
  [7],
  [2, 2, 3]
]

"""


'''
Created on Jan 23, 2017

@author: fanxueyi
'''


class Solution(object):
    def __init__(self):
        self.result=[]
        self.target = 0
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.target = target
        comb = []
        new_candidates = filter(lambda x: x<=target, candidates)
        self.helpFun(target, comb, new_candidates)
        return(self.result)
        
    def helpFun(self, target, comb, candidates):
        comb.sort()
        comb_sum = sum(comb)
        if comb_sum == self.target:
            if comb not in self.result:
                self.result.append(comb)
            return
        if comb_sum > self.target:
            return
            
        for i in candidates:
            tmp_target = target-i
            if tmp_target >= 0:
                new_comb = comb+[i]
                self.helpFun(tmp_target,new_comb, candidates)
            
            
            
            
s=Solution()
print(s.combinationSum([20,41,30,40,34,43,47,31,48,29,45,21,24,35,38,26,39,25,42,37,23,28,49,27,22,32,44,36], 70))

