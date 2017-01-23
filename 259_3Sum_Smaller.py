"""

Given an array of n integers nums and a target, find the number of index triplets i, j, k with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

For example, given nums = [-2, 0, 1, 3], and target = 2.

Return 2. Because there are two triplets which sums are less than 2:

[-2, 0, 1]
[-2, 0, 3]

"""
'''
Created on Jan 16, 2017

@author: fanxueyi
'''


class Solution(object):
    def threeSumSmaller(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        out = 0
        
        for i in range(len(nums)-2):
            tmp_sum = target - nums[i]
            p1 = i + 1
            p2 = len(nums) - 1 
            while p1 < p2:
                twoSum = nums[p1] + nums[p2]
                if twoSum < tmp_sum:
                    out += p2-p1
                    p1 += 1
                else:
                    p2 -= 1
                    
        return(out)
        
        