"""
找出出现奇数次的数字

"""

'''
Created on Mar 18, 2017

@author: fanxueyi
'''
class Solution(object):
    def findNumber(self,nums):
        if not nums:
            return
        res = 0
        for n in nums:
            res ^= n 
        return(res)
    

"""
两个数出现奇数次，其他偶数次，打印这两个数
"""
class Solution2(object):
    def findNumber(self,nums):
        diffAB = 0
        for n in nums:
            diffAB ^= n
        index = 0
        while diffAB != 0:
            if diffAB & 1 == 1:
                break
            else:
                index += 1
        mask = 1 << index
        diff0 = 0
        diff1 = 0
        
        for n in nums:
            if n & mask == 1:
                diff1 ^= n
            else:
                diff0 ^= n
        return(diff1, diff0)
                
        
        
        
        
        
        
        


