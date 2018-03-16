'''
Find the contiguous subarray within an array (containing at least one number) which has the largest sum.

For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
the contiguous subarray [4,-1,2,1] has the largest sum = 6.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

'''
#strategy: if the subarray must end at A[i], compare the sum with maxSum 
class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return(None)
        
        maxSum = preSum = nums[0]
        for i in range(1, len(nums)):
            if preSum < 0:
                preSum = nums[i]
            else:
                preSum += nums[i]
            maxSum = max(preSum, maxSum)
        return(max(maxSum, preSum))
        
