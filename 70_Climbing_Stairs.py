"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

"""

'''
Created on Jan 9, 2017

@author: fanxueyi
'''

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        maps = {}
        
        for i in range(n+1):
            maps[i] = -1
            
        return(self.helpFun(maps,n))
        
    def helpFun(self, maps, n):
        if n < 0:
            return 0
        elif n == 0:
            return 1
        elif maps[n] > -1:
            return maps[n]
        else:
            maps[n] = self.helpFun(maps,n-1) + self.helpFun(maps,n-2)
            return maps[n]
        
        
    def climbStairs2(self,n):
        if n < 1:
            return 0
        
        if n == 1 :
            return 1
        
        if n == 2:
            return 2
            
        climb1 = 1
        climb2 = 2
        
        for i in range(3, n+1):
            tmp = climb1 + climb2
            climb1 = climb2
            climb2 = tmp
        return tmp
    
    
        