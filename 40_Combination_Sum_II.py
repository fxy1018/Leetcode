"""
Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.

Each number in C may only be used once in the combination.

Note:
All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
For example, given candidate set [10, 1, 2, 7, 6, 1, 5] and target 8, 
A solution set is: 
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

"""
'''
Created on Jan 24, 2017

@author: fanxueyi
'''
class Solution(object):
    def __init__(self):
        self.result=[]
        self.target=0
    
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.target = target
        candidates = filter(lambda x: x<=target, candidates)
        candidates.sort()
        comb=[]
        self.helpFun(0,target, comb, candidates)
        return(self.result)
    
    def helpFun(self,index,target, comb, candidates):
        comb.sort()
        if sum(comb) == self.target and comb not in self.result:
            self.result.append(comb)
            return
        
        for i in range(index,len(candidates)):
            tmp_target = target-i
            if tmp_target >=0:
                new_comb = comb+[candidates[i]]
                self.helpFun(i+1, tmp_target, new_comb, candidates)
            
        
            
        
s= Solution()
print(s.combinationSum2([10,1,2,7,6,1,5], 8))
      

