"""

Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.


"""

'''
Created on Jan 30, 2017

@author: fanxueyi
'''


#http://fisherlei.blogspot.com/2013/01/leetcode-search-in-rotated-sorted-array.html

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
        #method 1: brute-force: O(n)
        for i in range(len(nums)):
            if nums[i] == target:
                return(i)
        return(-1)
        """
        
        #method2: binary search O(log(n))
        if len(nums)==0:
            return(-1)
            
        left = 0 
        right = len(nums)-1
        while left < right:
            mid = (left+right)//2
            if nums[mid] <= nums[right]:
                if nums[mid] < target and nums[right]>=target:
                    left = mid + 1
                else:
                    right = mid
            else:
                if nums[mid] >= target and nums[left] <= target:
                    right = mid
                else:
                    left = mid +1
                    
        if nums[left]==target:
            return(left)
        else:
            return(-1)
                
   class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return(-1)
        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return(mid)
            
            if nums[left] > nums[right]:
                if nums[mid] < nums[right]:
                    if nums[mid] > target:
                        right = mid-1
                        
                    else:
                        if nums[right] < target:
                            right = mid-1
                        else:
                            left = mid + 1
                else:
                    if nums[mid] < target:
                        left = mid+1
                    else:
                        if nums[left] > target:
                            left = mid+1
                        else:
                            right = mid-1
                        
            else:
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid -1 
                    
        return(-1)     
        
class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return(-1)
        
        left = 0
        right = len(nums)-1
        
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return(mid)
            if nums[mid] <= nums[right]:
                if nums[mid] < target and target <=nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                if nums[mid]>  target and target >= nums[left]:
                    right = mid-1
                else:
                    left = mid+1
        return(-1) 
