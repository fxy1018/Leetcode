"""

Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.

"""
'''
Created on Jan 21, 2017

@author: fanxueyi
'''


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        if n < 2:
            return(0)
            
        #method1: brute-force (Time Limit Exceeded O(n^2))
        #res = 0
        #for i in range(n-1):
        #    for j in range(i+1, n):
        #       if res < (j-i)*min(height[j],height[i]):
        #           res = (j-i)*min(height[j],height[i])
        #return(res)
                
        #methods2: two pointer
        
        p1 = 0
        p2 = len(height)-1
        res = (p2-p1)*min(height[p1],height[p2])
        while p1 < p2:
            res = max(res,(p2-p1)*min(height[p1],height[p2]))
            if height[p1] >= height[p2]:
                p2 -= 1
            else:
                p1 += 1
                
        return(res)                
                