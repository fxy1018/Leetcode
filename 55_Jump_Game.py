"""

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

For example:
A = [2,3,1,1,4], return true.

A = [3,2,1,0,4], return false.

"""
'''
Created on Feb 6, 2017

@author: fanxueyi
'''

"""
注意题目中A[i]表示的是在位置i，“最大”的跳跃距离，而并不是指在位置i只能跳A[i]的距离。所以当跳到位置i后，能达到的最大的距离至少是i+A[i]。用greedy来解，记录一个当前能达到的最远距离maxIndex：

1. 能跳到位置i的条件：i<=maxIndex。
2. 一旦跳到i，则maxIndex = max(maxIndex, i+A[i])。
3. 能跳到最后一个位置n-1的条件是：maxIndex >= n-1


"""
class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        maxIndex = 0
        for i in range(len(nums)):
            if i > maxIndex or maxIndex > len(nums)-1: 
                break
            maxIndex = max(maxIndex, nums[i]+i)
        
        return(maxIndex >= (len(nums)-1))