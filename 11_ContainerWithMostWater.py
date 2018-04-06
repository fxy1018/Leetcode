"""
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.


"""
#two points


class Solution:
    """
    @param heights: a vector of integers
    @return: an integer
    """
    def maxArea(self, heights):
        # write your code here
        length = len(heights)
        l = 0 
        r = length-1
        res = 0
        while l < r:
            res = max(res, (min(heights[l],heights[r]) * (r-l)))
            if heights[l] <heights[r]:
                l += 1
            else:
                r -= 1
        return(res)
