"""
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.


"""


'''
Created on Jan 16, 2017

@author: fanxueyi
'''


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #get the min dist from 3sum to target
        out  = target
        dist = 2**37-1
        nums.sort()
        for i in range(len(nums)-2):
            tmp_sum = target - nums[i]
            p1 = i + 1 
            p2 = len(nums)-1
            while p1 < p2:
                twoSum = nums[p1]+nums[p2]
                if (abs(tmp_sum-twoSum) < dist):
                    dist = abs(tmp_sum-twoSum)
                    out = twoSum + nums[i]
                if tmp_sum > twoSum:
                    p1 += 1
                elif tmp_sum < twoSum:
                    p2 -= 1
                else:
                    p1 += 1
                    p2 -= 1
        return(out)