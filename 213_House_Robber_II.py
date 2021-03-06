"""

Note: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new place for his thievery so that he will not get too much attention. This time, all houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, the security system for these houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

"""


'''
Created on Jan 14, 2017

@author: fanxueyi
'''

#in this question, the condition means if rob the first house, can't rob the last house, vice versa


class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return(0)
        if len(nums)==1:
            return(nums[0])
        return(max(self.helpFun(nums[1:]), self.helpFun(nums[:len(nums)-1])))
        
    def helpFun(self, nums):
        if not nums:
            return(0)
        if len(nums)==1:
            return(nums[0])
        a = nums[0]
        b = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            tmp = a
            a = b
            b = max(tmp+nums[i], b)
        
        return(b)
    
   class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if not nums:
            return(0)
        if len(nums) ==1:
            return(nums[0])
      
        #consider rob first house or not rob first house
        return(max(self.getMaxMoney(nums[1:]),  nums[0] + self.getMaxMoney(nums[2:-1])))
    
    def getMaxMoney(self, nums):
        
        if not nums:
            return(0)
        if len(nums) == 1:
            return(nums[0])
        
        prepre = nums[0]
        pre = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            curr = max(pre, prepre + nums[i])
            prepre = pre
            pre = curr
        
        return(pre) 
    
    
