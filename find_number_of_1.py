"""

given a 32 bits integer, it can be 0, positive or negative
return number of 1 in the integer

"""

'''
Created on Mar 18, 2017

@author: fanxueyi
'''
class Solution(object):
    def countOne(self,n):
        diffAB = 0
        for n in nums:
            diffAB ^= n
            
        mask = 1
        diff0 = diffAB
        diff1 = diffAB
        while diffAB & mask == 0:
            mask <<= 1
            
        for n in nums:
            if n & mask == 0:
                diff1 ^= n
            else:
                diff0 ^= n
                
        return([diff1, diff0])

    
s = Solution()
print(s.countOne2(3))









