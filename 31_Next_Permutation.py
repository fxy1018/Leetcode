"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place, do not allocate extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 -> 1,5,1

"""

'''
Created on Jan 23, 2017

@author: fanxueyi
'''

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        # refer: lexicographical permutation algorithm 
        #  https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
        
        n = len(nums)
        break_index = n-1
        for i in range(n-2, -1, -1):
            if nums[i]< nums[i+1]:
                for j in range(n-1, i,-1):
                    if nums[j] > nums[i]:
                        nums[i], nums[j] = nums[j],nums[i]
                        nums[i+1:] = sorted(nums[i+1:])
                        return
            else:
                break_index = i
        
        nums[:] = nums[::-1]
            
class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        lastIndex = -1
        for i in range(len(nums)-1):
            if nums[i+1] > nums[i]:
                lastIndex = i
        if lastIndex == -1:
            nums[:] = nums[::-1]
            return
        
        tmpNums = nums[lastIndex+1:][::-1]
        placeIndex = -1
        for i in range(len(tmpNums)):
            if tmpNums[i] > nums[lastIndex]:
                placeIndex = i
                break
        tmp = nums[lastIndex]
        nums[lastIndex] = tmpNums[placeIndex]
        tmpNums[placeIndex] = tmp
        nums[lastIndex+1:] = tmpNums
