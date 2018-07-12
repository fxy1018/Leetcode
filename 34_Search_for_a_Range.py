'''
Created on Jan 23, 2017

@author: fanxueyi
'''


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n = len(nums)
        left = 0
        right = n-1
        mid = (left+right)//2
        out = []
        while left <= right:
            if nums[mid] == target:
                out.append(mid)
                for i in range(mid+1, right+1):
                    if nums[i] == target:
                        out.append(i)

                for j in range(left, mid):
                    if nums[j] == target:
                        out.append(j)
                break
            elif nums[mid] > target:
                right = mid-1
            else:
                left = mid+1
            mid = (left+right)//2
           
        if len(out) == 0:
            return([-1,-1])
        else:
            out.sort()
            res = [out[0]]+[out[-1]]
            return(res)
        
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums)-1
        index = -1
        while left <= right:
            mid = (left+right)//2
            if target == nums[mid]:
                index = mid
                break
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        if index == -1:
            return([-1,-1])
        
        #find left bound
        left = 0
        right = index
        indexL = index
        while left <= right:
            mid = (left + right)//2
            if target == nums[mid]:
                indexL = mid
                right = mid -1
            elif target > nums[mid]:
                left = mid + 1
        #find right bount
        left = index
        right = len(nums)-1
        indexR = index
        while left <= right:
            mid = (left + right)//2
            if target == nums[mid]:
                indexR = mid
                left = mid + 1
            elif target < nums[mid]:
                right = mid - 1
        return([indexL, indexR])
                
class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #binary search twice: 
        #1. find last element smaller than target
        #2. find first element bigger than target
        
        #find last element smaller than target:
        left = 0
        right = len(nums)
        
        while left < right:
            mid = left + (right-left)//2
            if target > nums[mid]:
                left = mid +1
            else:
                right = mid
        leftBound = right 
        
        left = 0
        right = len(nums)
        while left < right:
            mid = left + (right-left)//2
            if target < nums[mid]:
                right = mid
            else:
                left = mid + 1
        rightBound = right -1
        
        if rightBound - leftBound < 0:
            return([-1,-1])
        else:
            return([leftBound, rightBound])
