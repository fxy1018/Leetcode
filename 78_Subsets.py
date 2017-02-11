"""
Given a set of distinct integers, nums, return all possible subsets.

Note: The solution set must not contain duplicate subsets.

For example,
If nums = [1,2,3], a solution is:

[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
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
    def subsets(self, nums):
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
        
        
    def helpFun(self, digits, index, comb, start):
        if index == digits:
            self.out.append(comb)
            return
        
        for i in range(start, self.n):
            
            new_comb = comb + [self.nums[i]]
            self.helpFun(digits, index+1, new_comb, i+1)
            
s = Solution()
print(s.subsets([1,2,3]))