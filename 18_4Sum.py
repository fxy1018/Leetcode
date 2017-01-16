"""
Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.


"""



'''
Created on Jan 16, 2017

@author: fanxueyi
'''

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        
        nums.sort()
        out = []
        for i in range(len(nums)-2):
            for j in range(i+1,len(nums)-1):
                tmp_sum = target-nums[i]-nums[j]
                p1 = j+1
                p2 = len(nums)-1
                while (p1 < p2) :
                    twoSum = nums[p1] + nums[p2]
                    if (tmp_sum == twoSum):
                        ans = [nums[i], nums[j], nums[p1], nums[p2]]
                        if ans not in out:
                            out.append(ans)
                        p1 += 1
                        p2 -= 1
                    elif (tmp_sum < twoSum):
                        p2 -= 1
                    else:
                        p1 += 1
                        
        return(out)
                    