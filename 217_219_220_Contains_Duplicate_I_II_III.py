"""
LC217:
Given an array of integers, find if the array contains any duplicates. Your function should return true if any value appears at least twice in the array, and it should return false if every element is distinct.

LC218:
Given an array of integers and an integer k, find out whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k.


"""

'''
Created on Jan 13, 2017

@author: fanxueyi
'''
class Solution217(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        return(len(nums) != len(set(nums)))

class Solution218(object):
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
    
 class Solution218_2(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numHash = {}
        for i in range(len(nums)):
            num = nums[i]
            if num in numHash and i-numHash[num] <=k:
                    return(True)
            numHash[num] = i
            
        return(False)
        
        
