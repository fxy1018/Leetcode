'''
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1

Input: [3,0,1]
Output: 2
Example 2

Input: [9,6,4,2,3,5,7,0,1]
Output: 8

Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?

'''

class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #math:
        total = (1+len(nums))*len(nums)//2
        if total == sum(nums):
            return(0)
        else:
            return(total-sum(nums))
            
class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #bit: similar to single number question. because number is 0-n and its index is also 0-n, so this two groups can be regards as groups of number, only one number is single, others are twice.
        
        miss = 0
        for n in nums:
            miss ^= n
        for i in range(1, len(nums)+1):
            miss ^= i
        return(miss)
