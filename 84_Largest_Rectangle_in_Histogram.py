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
            
  '''
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
'''

class Solution3(object):        
    def largestRectangleArea2(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        #time limit, O(n) = n^2
        if not heights:
            return(0)
        n = len(heights)
        out = []
        for i in range(n):
            count = 0
            for j in range(i, -1, -1):
                if heights[j] >= heights[i]:
                    count += 1
                else:
                    break
            for z in range(i+1, n):
                if heights[z] >= heights[i]:
                    count += 1
                else:
                    break
            out.append(heights[i] * count)
                
        return(max(out)) 
        
      #method2: use a stack to store left and right boundary
      class Solution(object):
    def largestRectangleArea2(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        heights.append(0)
        n = len(heights)
        stack = [-1]
        out = 0
        for i in range(n):
            curr = heights[i]
            while curr < heights[stack[-1]]:
                index = stack.pop()
                out = max(out, heights[index] * (i-stack[-1]-1))
            stack.append(i)
            
        heights.pop()
         
        return(out)
        
    
        
            
        
                
# s = Solution()
# print(s.largestRectangleArea([1,1]))          
#         
        
