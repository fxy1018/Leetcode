"""
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.


"""

'''
Created on Jan 13, 2017

@author: fanxueyi
'''
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if not nums:
            return(False)
        
        dic = {}
        
        for i in range(len(nums)):
            if nums[i] in dic:
                if abs(dic[nums[i]] - i) <= k:
                    return(True)
            dic[nums[i]] = i
        
        return(False)
        
        