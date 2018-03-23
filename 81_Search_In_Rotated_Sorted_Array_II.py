"""

Follow up for "Search in Rotated Sorted Array":
What if duplicates are allowed?

Would this affect the run-time complexity? How and why?
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Write a function to determine if a given target is in the array.

The array may contain duplicates.

Show Tags
Hide Similar Problems

"""



'''
Created on Feb 24, 2017

@author: fanxueyi
'''


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        #analysis: we can't decide whether the left part arr or right part arr is sorted, so the worst case of this question is O(n)
        
        #method1: O(n)
        for n in nums:
            if n == target:
                return(True)
        return(False)
        
    #method2: average O(logN)
    
    def search2(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        
        left = 0
        right = len(nums)-1
        
        while left<=right:
            mid = (right+left)//2
            
            if nums[mid] == target:
                return(True)
            
            if nums[mid] < nums[right]: # right half has sorted
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                elif nums[mid] == target:
                    return(True)
                else:
                    right = mid-1
            elif nums[mid] > nums[right]: #left half has sorted
                if nums[mid] > target and target>= nums[left]:
                    right = mid - 1
                elif nums[mid] == target:
                    return(True)
                else:
                    left = mid + 1
            else:
                right -= 1
                
        return(False)
 class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
       
        if not nums:
            return(False)
        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return(True)
            if nums[mid] < nums[right]:
                if nums[mid] < target and target <=nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] > nums[right]:
                if nums[mid]>  target and target >= nums[left]:
                    right = mid-1
                else:
                    left = mid+1
            else:
                right -= 1
                
        return(False)       
