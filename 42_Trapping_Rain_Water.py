"""

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

For example, 
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.


"""
'''
Created on Feb 11, 2017

@author: fanxueyi
'''

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 3:
            return 0
        
        n = len(height)
        R_MAX = [0]*n
        L_MAX = [0]*n
        sum = 0 
        # time exceed, don't need to compare so much
        for i in range(1,n):
            L_MAX[i] = max(height[0:i])
        
        for j in range(n-2, -1, -1):
            R_MAX[j] = max(height[j:])
            
        for h in range(1, n-1):
            l_max = L_MAX[h]
            r_max = R_MAX[h]
            h_max = min(l_max, r_max)
            
            if h_max > height[h]:
                sum += h_max-height[h]
        return(sum)
    
class Solution2(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 3:
            return 0
        
        n = len(height)
        R_MAX = [0]*n
        L_MAX = [0]*n
        sum = 0 
        for i in range(1,n):
            L_MAX[i] = max(L_MAX[i-1], height[i-1])
        
        for j in range(n-2, -1, -1):
            R_MAX[j] = max(R_MAX[j+1], height[j+1])
        
        #still reduancy
        for h in range(1, n-1):
            l_max = L_MAX[h]
            r_max = R_MAX[h]
            h_max = min(l_max, r_max)
            
            if h_max > height[h]:
                sum += h_max-height[h]
                
        return(sum)
    
class Solution3(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height or len(height) < 3:
            return 0
        
        n = len(height)
        R_MAX = [0]*n
        L_MAX = [0]*n
        sum = 0 
        for i in range(1,n):
            L_MAX[i] = max(L_MAX[i-1], height[i-1])
        
        for j in range(n-2, -1, -1):
            R_MAX[j] = max(R_MAX[j+1], height[j+1])
            h_max = min(L_MAX[j], R_MAX[j])
            if h_max > height[j]:
                sum += h_max-height[j]
                
        return(sum)
        
        