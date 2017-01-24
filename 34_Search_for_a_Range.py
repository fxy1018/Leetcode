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