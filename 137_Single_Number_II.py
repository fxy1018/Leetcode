# Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''
Created on Jan 6, 2017

@author: fanxueyi
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #return((sum(set(nums))*3 - sum(nums))/2)
        
        #bit manipulation
        ans = 0
        for i in range(32):
            sum = 0
            for num in nums:
                sum += (num>>i) & 1
            sum %= 3 
            ans |= sum << i
        #return(self.convert(ans))
        return(self.convert(ans))
        
    def convert(self, x):
        if x>= 2**31:
            x -= 2**32
        return(x)
        