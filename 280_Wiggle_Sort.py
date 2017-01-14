"""
Given an unsorted array nums, reorder it in-place such that nums[0] <= nums[1] >= nums[2] <= nums[3]....

For example, given nums = [3, 5, 2, 1, 6, 4], one possible answer is [1, 6, 2, 5, 3, 4].
"""

'''
Created on Jan 14, 2017

@author: fanxueyi
'''

class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        i = 1
        nums.sort()
        
        while len(nums)!= 0 and len(nums)!= 1 and i <len(nums)-1:
            nums[i],nums[i+1] = nums[i+1],nums[i]
            i += 2
        
        
    def wiggleSort2(self, nums):
        for i in range(len(nums)):
            nums[i:i+2] = sorted(nums[i:i+2], reverse=i%2)