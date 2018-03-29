'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

Find the minimum element.

You may assume no duplicate exists in the array.

'''


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return(min(nums))
#method2: binary search
class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]
        left = 0
        right= len(nums)-1
        
        while left <=right:
            mid = (left + right)//2
            if nums[left] < nums[right]:
                res = min(nums[left], res)
                return(res)
            else:
                if nums[mid] < nums[right]:
                    res = min(nums[mid], res)
                    right = mid-1
                else:
                    left = mid+1
        return(min(res, nums[left-1]))
