"""

给定一个长度为N（N>1）的整型数组arr，可以划分成左右两个部分，左部分为
arr[0..K]，右部分为arr[K+1..N-1]，K可以取值的范围是[0,N-2]。求这么多划分方
案中，左部分中的最大值减去右部分最大值的绝对值中，最大是多少？

"""
'''
Created on Feb 14, 2017

@author: fanxueyi
'''

class Solution(object):
    def maxABS1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #brute-force O(n^2)
        if not nums or len(nums) < 2:
            return(None)
        res = -float("Inf")
        max_l = 0
        max_r = 0
        
        for i in range(1,len(nums)-1):
            #in python time complexity of max or min is O(n)
            max_l = max(nums[0:i])
            max_r = max(nums[i:])
            res = max(res, abs(max_l-max_r))
        return(res)  
        
    def maxABS2(self, nums):
        # 预处理arr
        n = len(nums)
        max_l = [0 for i in range(n)]
        max_l[0] = nums[0]
        max_r = [0 for i in range(n)]
        max_r[-1] = [nums[-1]]
        res = -float("Inf")
        for i in range(1,n):
            max_l.append(max(max_l[i-1], nums[i]))
        for i in range(n-2,-1,-1):
            max_r.append(max(max_r[i+1], nums[i]))
            res = max(res, abs(max_r[i]-max_l[i]))
        return(res)
    
    def maxABS3(self,nums):
        #巧思， max 与头尾对比
        max_num = max(nums)
        return(max_num-min(nums[0], nums[-1]))
     
        