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
 
#method2: bit manipulation

class Solution2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return([])
        out = []
        n = len(nums)
        for i in range(2**n):
            bit = bin(i)[2:]
            if len(bit) < n:
                bit = "0" * (n-len(bit)) + bit
            tmp = []
            for j in range(n):
                if bit[j] != "0":
                    tmp.append(nums[j])   
            out.append(tmp)
        return(out)
class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
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
print(s.subsets([1,2,3]))
