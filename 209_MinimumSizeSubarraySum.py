'''
Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

For example, given the array [2,3,1,2,4,3] and s = 7,
the subarray [4,3] has the minimal length under the problem constraint.

click to show more practice.

More practice:
If you have figured out the O(n) solution, try coding another solution of which the time complexity is O(n log n).
'''

class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        window = []
        currSum = 0
        i = 0
        res = len(nums) + 1
        while i < len(nums):
            if currSum < s:
                window.append(i)
                currSum += nums[i]
                i += 1
            else:
                res = min(res, window[-1] - window[0] + 1)
                currSum -= nums[window[0]]
                window = window[1:]
            
        while len(window)>0:
            if currSum >=s:
                res = min(res, window[-1] - window[0] + 1)
            currSum -= nums[window[0]]
            window = window[1:]
            
        if res == len(nums) + 1:
            return(0)
        
        return(res)        
        
        
#modify, use pointer instead of array
class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        currSum = 0
        left = 0
        n = len(nums)
        res = n + 1
        for i in range(n):
            currSum += nums[i]
            while currSum >= s:
                res = min(res, i-left + 1)
                currSum -= nums[left]
                left += 1
            
        if res == len(nums) + 1:
            return(0)
        
        return(res)        
