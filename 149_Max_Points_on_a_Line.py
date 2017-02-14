"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.

"""

'''
Created on Feb 13, 2017

@author: fanxueyi
'''


import numpy as np
# Definition for a point.
class Point(object):
     def __init__(self, a=0, b=0):
         self.x = a
         self.y = b

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        maxPoints = 0
        n = len(points)
        
        for i in range(n):
            slope_hash = {}
            nVertical, nSame, nMax = 0, 0 ,0
            for j in range(i+1, n):
                if points[i].x == points[j].x:
                    if points[i].y != points[j].y:
                        nVertical += 1
                    else:
                        nSame += 1
                else:
                    slope = np.longdouble(points[j].y-points[i].y)/np.longdouble((points[j].x-points[i].x))
                    print(slope)
                    slope_hash[slope] = slope_hash.get(slope, 0) + 1
                    nMax = max(nMax, slope_hash[slope])
            maxPoints = max(maxPoints, max(nMax, nVertical)+nSame+1)
        return(maxPoints)
   
s=Solution()
print(s.maxPoints([Point(0,0),Point(94911151,94911150),Point(94911152,94911151)]))  