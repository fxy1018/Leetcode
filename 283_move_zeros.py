"""

Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

For example, given nums = [0, 1, 0, 3, 12], after calling your function, nums should be [1, 3, 12, 0, 0].

Note:
You must do this in-place without making a copy of the array.
Minimize the total number of operations.


"""
'''
Created on Feb 16, 2017

@author: fanxueyi
'''
class Solution(object):
    #method1:
    def moveZeroes1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                count += 1
                nums.pop(i)
        
        nums += [0]*count
        
    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        p_0 = 0
        p_1 = 0
        n = len(nums)
        
        while p_0 < n and p_1 < n:
            if nums[p_0] != 0:
                p_0 += 1
                p_1 = p_0
                continue
            if nums[p_1] == 0:
                p_1 += 1
                continue
            
            nums[p_0], nums[p_1] = nums[p_1], nums[p_0]
            p_0 += 1
            p_1 += 1
            
            
        
        
        
                
        