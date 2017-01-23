"""

Given a collection of numbers that might contain duplicates, return all possible unique permutations.

For example,
[1,1,2] have the following unique permutations:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]

"""


'''
Created on Jan 23, 2017

@author: fanxueyi
'''

class Solution(object):
    def __init__(self):
        self.result=[]
        self.n = 0
        self.created=[]
    
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        self.n = len(nums)
        comb=[]
        self.helpFun(nums, 0, comb)
        return(self.result)
        
    def helpFun(self, nums, index, comb):
        if index == self.n:
            self.result.append(comb)
            return
        for i in range(len(comb)+1):
            if i ==0 :
                new_comb = [nums[index]] + comb
            elif i == len(comb):
                new_comb = comb + [nums[index]]
            else:
                new_comb = comb[0:i]+[nums[index]]+comb[i:]
            if new_comb not in self.created:
                self.created.append(new_comb)
                self.helpFun(nums, index+1, new_comb)
        
            
            
            