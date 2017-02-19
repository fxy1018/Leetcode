"""

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

"""



'''
Created on Feb 18, 2017

@author: fanxueyi
'''


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        max_len = 0
        
        while nums:
            num = nums.pop()
            curr_len = 1
            left_num = num - 1
            right_num = num + 1
            while left_num in nums:
                nums.remove(left_num)
                left_num -= 1
                curr_len += 1
            while right_num in nums:
                nums.remove(right_num)
                right_num += 1
                curr_len += 1
            max_len = max(curr_len, max_len)
        return(max_len)