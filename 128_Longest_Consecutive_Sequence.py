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
    
class Solution:
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = {}
        right = {}
        nums = set(nums)
        res = 0
        for num in nums:
            if num+1 in left:
                #check left:
                left[num] = left[num+1] + 1
                right[num+left[num+1]] = left[num+1] + 1
                res = max(res, left[num+1] + 1)
                
            if num-1 in right:
                #check right:
                right[num] = right[num-1] + 1
                left[num-right[num-1]] = right[num-1] + 1
                res = max(res, right[num-1] + 1)
            #check whether two interval can merge:
            if num in left and num in right:
                tmp1 = left[num]
                tmp2 = right[num]
                del(left[num])
                del(right[num])
                new = tmp2 + tmp1-1
                left[num-tmp2+1] = new
                right[num + tmp1-1] = new               
                res = max(res, new)
                
            if num+1 not in left and num-1 not in right:
                left[num] = 1
                right[num] = 1
                res = max(res, 1)
        
        return(res)
        
