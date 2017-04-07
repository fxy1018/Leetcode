"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

For example,
Given [10, 9, 2, 5, 3, 7, 101, 18],
The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4. Note that there may be more than one LIS combination, it is only necessary for you to return the length.

Your algorithm should run in O(n2) complexity.

Follow up: Could you improve it to O(n log n) time complexity?


"""



'''
Created on Mar 25, 2017

@author: fanxueyi
'''


class Solution(object):
    #O(N^2) DP 解法
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return(0)
            
        dp = [1] * len(nums)
        
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j]+1)
        
        return(max(dp))
    
    
    #O(nlogN) 解法， binary serach
    def lengthOfLIS2(self,nums):
    
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return(0)
            
        ends = [nums[0]]
        r = 0
        for i in range(1,len(nums)):
            left = 0
            right = len(ends)-1
            while (left <= right):
                mid = (left+right)//2
                if ends[mid] < nums[i]:
                    left = mid + 1
                else:
                    right = mid - 1
           
            if left >= len(ends):
                ends.append(nums[i])
            else:
                ends[left] = nums[i]
        
        return(len(ends))

s=Solution()
print(s.lengthOfLIS2([10, 9, 2, 5, 3, 7, 101, 18]))