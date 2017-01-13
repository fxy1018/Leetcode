"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

"""

'''
Created on Jan 13, 2017

@author: fanxueyi
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return(0)
        if len(nums) == 1:
            return(nums[0])
        if len(nums) == 2:
            return(max(nums[0], nums[1]))
            
        val = [nums[0], max(nums[0], nums[1])]
        
        for i in range(2, len(nums)):
            vmax = max(val[i-2]+nums[i], val[i-1])
            val.append(vmax)
            
        return(val[-1])



    #actually it only need to get val[i-1] and val[i-2]]
    
    def rob2(self,nums):
        
        v1 = nums[0]
        v2 = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            tmp = v2
            v2 = max(v1+nums[i], v2)
            v1 = tmp
        
        return(v2)