"""

Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note:
You are not suppose to use the library's sort function for this problem.

click to show follow up.

Follow up:
A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with an one-pass algorithm using only constant space?

"""



'''
Created on Jan 25, 2017

@author: fanxueyi
'''



class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        #method1: two-pass algorithm using counting sort
        #dict_num = {0:0,1:0,2:0}
        #for i in nums:
        #    dict_num[i]+=1
        #index = 0 
        #for i in range(3):
        #    for j in range(dict_num[i]):
        #        nums[index] = i
        #        index +=1
                
        #method2: 
        left = 0
        right = len(nums)-1
        curr = 0
        while curr <= right:
            if nums[curr] ==0:
                nums[left], nums[curr] = nums[curr], nums[left]
                curr += 1
                left += 1
            elif nums[curr] == 1:
                curr += 1
            elif nums[curr] == 2:
                nums[right], nums[curr] = nums[curr], nums[right]
                right -= 1
                