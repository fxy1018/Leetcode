'''

Given an array consisting of n integers, find the contiguous subarray of given length k that has the maximum average value. And you need to output the maximum average value.

Example 1:
Input: [1,12,-5,-6,50,3], k = 4
Output: 12.75
Explanation: Maximum average is (12-5-6+50)/4 = 51/4 = 12.75
Note:
1 <= k <= n <= 30,000.
Elements of the given array will be in the range [-10,000, 10,000].

'''
class Solution:
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        #method1: brute-force
        if k > len(nums):
            return()
        preSum = 0
        maxSum = -float("Inf")
        
        for i in range(0, len(nums)-k+1):
            preSum = sum(nums[i: i+k])
            maxSum = max(maxSum, preSum)
        return(maxSum/k)

    def findMaxAverage2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        #method2: store record to increase speed
        if k > len(nums):
            return()
        preSum = sum(nums[0:k])
        maxSum = preSum
        
        for i in range(k, len(nums)):
            preSum = preSum + nums[i] - nums[i-k]
            maxSum = max(maxSum, preSum)
        return(maxSum/k)
