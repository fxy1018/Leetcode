'''
Given a sorted array consisting of only integers where every element appears twice except for one element which appears once. Find this single element that appears only once.

Example 1:

Input: [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: [3,3,7,7,10,11,11]
Output: 10
Example
Your solution should run in O(log n) time and O(1) space.

'''
class Solution:
    """
    @param nums: a list of integers
    @return: return a integer
    """
    def singleNonDuplicate(self, nums):
        # write your code here
        n = nums[0]
        for i in range(1, len(nums)):
            n ^= nums[i]
        return(n)
        
        
class Solution:
    """
    @param nums: a list of integers
    @return: return a integer
    """
    def singleNonDuplicate(self, nums):
        # write your code here
        if not nums:
            return()
 
        left = 0
        right = len(nums)-1
        
        while left < right:
            mid = left + (right-left)//2
            if (right-mid)%2 == 1: #odd
               
                if nums[mid] == nums[mid + 1]:
                    right = mid - 1 
                elif nums[mid] == nums[mid-1]:
                    left = mid + 1
                else:
                    return(nums[mid])
            else:  #even
                if nums[mid] == nums[mid + 1]:
                    left = mid + 2 
                elif nums[mid] == nums[mid-1]:
                    right = mid - 2
                else:
                    return(nums[mid])
        return(nums[left])
