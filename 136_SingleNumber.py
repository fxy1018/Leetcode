'''
Given an array of integers, every element appears twice except for one. Find that single one.

Note:
Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

'''
#hash:
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #hash
        numHash = {}
        for n in nums:
            numHash[n] = numHash.get(n, 0)+1
        for n in numHash:
            if numHash[n] == 1:
                return(n)
                
#bit
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #bit
        res = nums[0]
        
        for i in range(1, len(nums)):
            res ^= nums[i]
        return(res)
