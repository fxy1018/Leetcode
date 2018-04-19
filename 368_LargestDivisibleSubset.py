'''
Given a set of distinct positive integers, find the largest subset such that every pair (Si, Sj) of elements in this subset satisfies: Si % Sj = 0 or Sj % Si = 0.

If there are multiple solutions, return any subset is fine.

Example 1:

nums: [1,2,3]

Result: [1,2] (of course, [1,3] will also be ok)
Example 2:

nums: [1,2,4,8]

Result: [1,2,4,8]

'''
#brute force, TLE
class Solution:
    def largestDivisibleSubset(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 2:
            return(nums)
        
        nums = sorted(nums)
        l = len(nums)
        self.res = []
        self.helpFun(nums, l, 0, [])
        return(self.res)
    
    def helpFun(self, nums, l, index, curr):
        if index == l:
            if len(self.res) < len(curr):
                self.res = curr
            return
        
        for i in range(index, l):
            #not select
            self.helpFun(nums, l, index+1, curr)
            #select
            if not curr:
                newCurr = curr + [nums[index]]
                self.helpFun(nums, l, index+1, newCurr)
            else:
                if nums[index]%curr[-1] == 0:
                    newCurr = curr + [nums[index]]
                    self.helpFun(nums, l, index+1, newCurr)
 #memorized
 
 
                
