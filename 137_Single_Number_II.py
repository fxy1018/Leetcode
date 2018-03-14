# Given an array of integers, every element appears three times except for one, which appears exactly once. Find that single one.
# 
# Note:
# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?
'''
Created on Jan 6, 2017

@author: fanxueyi
'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """    
        #bit manipulation: 充分利用数组元素是int类型这一特点，统计所有元素的第i个bit上为1的个数，因为题目说了其它元素出现了3次，而特殊元素只出现了1次，所以当统计的个数不能整除3就表明特殊元素在第i个bit上是1，所以我们把结果的第i个bit设为1，通过检查32个bit，这样我们就构造出了特殊元素，最后返回结果即可，时间复杂度是O（32n）
        ans = 0
        for i in range(32):
            sum = 0
            for num in nums:
                sum += (num>>i) & 1
            sum %= 3 
            ans |= sum << i
        #return(self.convert(ans))
        return(self.convert(ans))
        
    def convert(self, x):
        if x>= 2**31:
            x -= 2**32
        return(x)
        
   def singleNumber2(self, nums):
        #method1: Math
        return((sum(set(nums))*3 - sum(nums))/2)
   def singleNumber3(self, nums):     
        #method3: hash
        numHash = {}
        for n in nums:
            numHash[n] = numHash.get(n, 0) + 1
        for key in numHash:
            if numHash[key] == 1:
                return(key)
