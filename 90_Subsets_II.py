"""

Given a collection of integers that might contain duplicates, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,2], a solution is:

[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

"""


'''
Created on Feb 11, 2017

@author: fanxueyi
'''
class Solution(object):
    def __init__(self):
        self.out = []
        self.nums = []
        self.n = 0
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.nums = nums
        self.n = len(nums)
        for i in range(self.n+1):
            comb = []
            self.helpFun(i, 0, comb, 0)
        return(self.out)
        
    #method1: too slow   
    def helpFun(self, digits, index, comb, start):
        if index == digits:
            comb = sorted(comb)
            if comb not in self.out:
                self.out.append(comb)
            return
        
        for i in range(start, self.n):
            
            new_comb = comb + [self.nums[i]]
            self.helpFun(digits, index+1, new_comb, i+1)
            
class Solution:
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        res = [[]]
        self._helpFun(nums,  res, [])
        return(res)
    
    def _helpFun(self, nums, res, curr):
        if not nums:
            if curr not in res:
                res.append(curr)
            return
        
        for i in range(len(nums)):
            newCurr = curr + [nums[i]]
            if newCurr not in res:
                res.append(newCurr)
            
            self._helpFun(nums[i+1:], res, newCurr )     
            
s = Solution()
print(s.subsetsWithDup([4,4,4,1,4]))
