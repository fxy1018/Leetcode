"""

84. Largest Rectangle in Histogram

Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.

For example,
Given heights = [2,1,5,6,2,3],
return 10.

"""
'''
Created on Mar 4, 2017

@author: fanxueyi
'''

import pdb
pdb.set_trace()

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return(0)
            
        if len(heights) == 1:
            return(heights[0])
            
        stack = [0]
        res = heights[0]
        
        for i in range(1,len(heights)):
            
            if heights[i] < heights[stack[-1]]:
                pop_index = stack.pop()
                if not stack:
                    res = max(heights[pop_index] * i , res)
                else: 
                    res = max(heights[pop_index] * (i-stack[-1]-1), res)
                    
                    while stack and heights[i] <= heights[stack[-1]] :
                        pop_index = stack.pop()
                        if not stack:
                            res = max(heights[pop_index] * i , res)
                        else: 
                            res = max(heights[pop_index] * (i-stack[-1]-1), res)
                                          
            stack.append(i)

        
        i = len(heights)
        pop_index = stack.pop()
        if not stack:
            res = max(heights[pop_index] * i , res)
        else: 
            res = max(heights[pop_index] * (i-stack[-1]-1), res)
            while stack and 0 <= heights[stack[-1]]:
                pop_index = stack.pop()
                if not stack:
                    res = max(heights[pop_index] * i , res)
                else: 
                    res = max(heights[pop_index] * (i-stack[-1]-1), res)
                                                         
        return(res)
    

##modified the code
class Solution2(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        
        stack = [0]
        res = heights[0]
        
        for i in range(1,len(heights)):
            while stack and heights[i] <= heights[stack[-1]] :
                pop_index = stack.pop()
                if not stack:
                    res = max(heights[pop_index] * i , res)
                else: 
                    res = max(heights[pop_index] * (i-stack[-1]-1), res)
            stack.append(i)
        return(res)
            
        
            
        
                
s = Solution()
print(s.largestRectangleArea([1,1]))          
        
        