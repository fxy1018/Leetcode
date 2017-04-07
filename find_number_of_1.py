b"""

given a 32 bits integer, it can be 0, positive or negative
return number of 1 in the integer

"""

'''
Created on Mar 18, 2017

@author: fanxueyi
'''
class Solution(object):
    def countOne(self,n):
        count = 0
        for i in range(32):
            if n & 1:
                count += 1
            n >>= 1
        return(count)
    
    def countOne2(self,n):
        nStr = bin(n)[2:]
        return(nStr.count("1"))

    
s = Solution()
print(s.countOne(9))
print(s.countOne2(9))









