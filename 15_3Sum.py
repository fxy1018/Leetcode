"""
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

"""

'''
Created on Jan 16, 2017

@author: fanxueyi
'''

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        nums.sort()
        out = []
        for i in range(len(nums)-2):
            tmp_sum = 0 - nums[i]
            p1 = i+1
            p2 = len(nums)-1
            while p1 < p2:
                twoSum = nums[p1]+nums[p2]
                if ( twoSum == tmp_sum):
                    ans = [nums[i], nums[p1], nums[p2]]
                    if ans not in out:
                        out.append(ans)
                    p1 += 1
                    p2 -= 1
                elif (twoSum < tmp_sum):
                    p1 += 1
                else:
                    p2 -= 1
                    
        return(out)
          
        
         