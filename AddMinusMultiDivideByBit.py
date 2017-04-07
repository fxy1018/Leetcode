"""
use bit manipulation to implement add, minus, product, divide

"""
'''
Created on Mar 22, 2017

@author: fanxueyi
'''


class Solution(object):
    def add(self, a, b):        
        sum = a
        while (b!= 0) :
            sum = a ^ b
            b = (a & b) << 1
            a = sum
        return(sum)
    
    def negNum(self,n):
        return(self.add(~n,1))
    
    def minus(self,a,b):
        return(self.add(a, self.negNum(b)))
    
    
    
    ###problem of negative multi, seem something wrong with python int
    def multi(self,a,b):
        count = 0
        res = 0
        while (b!=0) and count < 32:
            count += 1
            if ( (b & 1) != 0):
                res = add(res, a)
            a <<= 1
            b >>= 1
        return(res)
    
    
s = Solution()
print(s.add(-2,-5))
print(s.negNum(-2))
print(s.multi(2,-3))
        
