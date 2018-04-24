'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

time: O(N)
space: O(N)
'''

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numHash = {}
        for i in range(len(nums)):
            n = nums[i]
            numHash[n] = numHash.get(n, []) + [i]
        for i in range(len(nums)):
            n = nums[i]
            if target-n in numHash:
                if target-n == n and len(numHash[target-n]) > 1:
                    return([i, numHash[target-n][-1]])
                elif target-n == n and len(numHash[target-n]) <= 1:
                    continue
                else:
                    return([i, numHash[target-n][0]])
                
