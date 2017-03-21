"""

given two 32bits integer a, b. return larger one

"""
from dask.array.ufunc import signbit
from _signal import SIGBUS

'''
Created on Mar 18, 2017

@author: fanxueyi
'''

class Solution(object):
    #这个方法有数据溢出的风险
    def compareAB1(self,a,b):
        '''
        input: int, int
        rType: int
        
        '''
        
        c = a - b
        sigA = self.sign(c)
        sigB = self.flip(sigA)
        return(a*sigA + b*sigB)
    
    def flip(self,n):
        return(n^1)
    
    def sign(self,n):
        return(self.flip((n>>31) & 1))


    def compareAB2(self,a,b):
        '''
        input: int, int
        rType: int
        
        '''
        c = a - b
        sigA = self.sign(a)
        sigB = self.sign(b)
        sigC = self.sign(c)
        diffAB = sigA ^ sigB 
        sameAB = self.flip(diffAB)
        returnA = diffAB * sigA + sameAB * sigC
        returnB = self.flip(returnA)
        return(a * returnA + b * returnB)
        
s = Solution()
print(s.compareAB2(8,4))