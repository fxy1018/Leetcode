#Given an array nums and a target value k, find the maximum length of a subarray that sums to k. If there isn't one, return 0 instead.

#Note:
#The sum of the entire nums array is guaranteed to fit within the 32-bit signed integer range.

#Example 1:
#Given nums = [1, -1, 5, -2, 3], k = 3,
#return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

#Example 2:
#Given nums = [-2, -1, 2, 1], k = 1,
#return 2. (because the subarray [-1, 2] sums to 1 and is the longest)

#Follow Up:
#Can you do it in O(n) time?



'''
Created on Jan 5, 2017

@author: fanxueyi

'''


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        pos_hash = {0:0}
        out = None 
        temp_sum = 0
        
        for i in range(len(nums)):
            temp_sum += nums[i]
            remain_sum = temp_sum - k
            if remain_sum in pos_hash:
                length = i + 1 - pos_hash[remain_sum]
                if out is None or length > out:
                    out = length
            if temp_sum not in pos_hash:
                pos_hash[temp_sum] = i + 1
                
        return(out or 0)
        

