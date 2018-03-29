'''
A peak element is an element that is greater than its neighbors.

Given an input array where num[i] ≠ num[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that num[-1] = num[n] = -∞.

For example, in array [1, 2, 3, 1], 3 is a peak element and your function should return the index number 2.

click to show spoilers.

Note:
Your solution should be in logarithmic complexity.

'''

class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #method1: linear
        if len(nums)==1:
            return(0)
        
        for i in range(len(nums)):
            if i == 0:
                if nums[i+1] < nums[i]:
                    return(i)
            elif i == len(nums)-1:
                if nums[i-1] < nums[i]:
                    return(i)
            elif nums[i-1] < nums[i] and nums[i+1] < nums[i]:
                return(i)
                
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #method1: binary search
        l = 0
        r = len(nums)-1
        while l<r:
            mid = (l+r)//2
            if nums[mid] > nums[mid+1]:
                r = mid
            else:
                l = mid+1

        return(l)
    
